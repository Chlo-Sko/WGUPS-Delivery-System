from Package import Package
from Distance import Distance
import datetime

distance = Distance()

class Truck:
    # Initiates Truck Object
    def __init__(self, t_id):
        self.t_id = t_id
        self.capacity = 16
        self.speed = 18

        self.start_time = []
        self.tot_time = []
        self.curr_time = []
        self.start_time_delta = []
        self.sum_time = None

        self.packages: list[Package] = []
        self.next_package = 0

        self.stops = []

        self.curr_loc = 0
        self.prev_loc = 0
        self.next_loc = 0
        self.tot_dist = 0

    # Prints truck object: O(1)
    def __str__(self):
        return f'Truck {self.t_id} Status: Packages on Truck: {len(self.packages)}, Current Location: {self.curr_loc}, Next Location: {self.next_loc}, Total Distance: {self.tot_dist}, Current Time: {self.curr_time},Total Time: {self.sum_time}'

    # Returns true if the truck's capacity is equal to or less than 0: O(1)
    def is_full (self):
        return self.capacity <= 0

    # Returns the total distance traveled by the truck object: O(1)
    def get_tot_dist(self):
        return round(self.tot_dist, 2)

    # Adds provided distance to truck's total distance: O(1)
    def add_to_dist(self, dist):
        self.tot_dist += float(dist)

    # Sends the truck back to the "hub", adds distance and time to truck object: O(1)
    def return_to_hub (self):
        self.prev_loc = self.curr_loc
        self.curr_loc = 0
        self.next_loc = 0
        dist_trav = Distance.get_dist(distance, self.prev_loc, self.curr_loc)
        self.add_to_dist(dist_trav)
        del_time = self.get_delivery_time(dist_trav)
        self.get_total_time(del_time)
        if self.packages:
            print('Error! Truck', self.t_id, 'has',len(self.packages), 'packages remaining on it.')

    # Loads provided object onto truck if truck is not full, adds package object information to package and stops lists, iterates the package list to set truck's next destination: O(n)
    def load_package(self, package):
        if self.is_full():
            print('Cannot load package:', package.get_id(), '- Truck', self.t_id, 'is full')
        else:
            package.load(self)
            self.packages.append(package)
            self.stops.append(package.get_address())
            self.capacity = 16 - len(self.packages)
            self.next_package = self.get_next_package()

    # Sets the truck's next direction by iterating the truck's package objects and finding the nearest neighbor to the truck's current location: O(n)
    def set_next_loc(self):
        self.next_loc = distance.get_loc_num(self.packages[0].get_address())
        self.next_package = self.packages[0]
        for p in self.packages:
           address = p.get_address()
           loc_num = distance.get_loc_num(address)
           dist = distance.get_dist(loc_num, self.curr_loc)
           if dist < distance.get_dist(self.next_loc, self.curr_loc):
               self.next_loc = loc_num
               self.next_package = p

    # Sets the truck's next direction and returns the package object needing to be delivered to this location: O(n)
    def get_next_package(self):
        self.set_next_loc()
        return self.next_package

    # Unloads package from the truck if it is on the truck, adds delivery distances and time to truck object, sets next package to be delivered: O(n)
    def unload_package(self, package):
        if package not in self.packages:
            print('Could not unload package', package.get_id, 'as it is not in Truck', self.t_id)
        else:
            self.capacity = 16 - len(self.packages)

            self.prev_loc = self.curr_loc
            self.curr_loc = distance.get_loc_num(package.get_address())
            dist_trav = distance.get_dist(self.curr_loc, self.prev_loc)
            self.add_to_dist(dist_trav)

            del_time = self.get_delivery_time(dist_trav)
            self.get_total_time(del_time)

            package.deliver(self)

            self.packages.remove(package)
            self.stops.remove(package.get_address())

            if self.packages:
                self.next_package = self.get_next_package()

    # Unloads all packages from truck based on nearest neighbor and returns the truck to the hub once all packages are delivered: O(n)
    def unload_truck(self):
           while self.capacity < 14:
               self.unload_package(self.next_package)
           self.unload_package(self.packages[0])
           self.return_to_hub()

    # Takes a provided distance and uses the truck object's speed to calculate the amount of time it took to go the distance: O(1)
    def get_delivery_time(self, dist):
        del_time = dist / self.speed
        dist_min = '{0:02.0f}:{1:02.0f}'.format(*divmod(del_time * 60, 60))
        formatted_time = dist_min + ':00'
        return formatted_time

    # Takes a provided time and adds it to the truck's total time: O(n)
    def get_total_time(self, time):
        self.tot_time.append(time)
        self.sum_time = datetime.timedelta()
        for i in self.tot_time:
            (h, m, s) = i.split(':')
            d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            self.sum_time += d
        self.curr_time = self.sum_time
        return self.sum_time

    # Sets the truck object's start time to the provided time: O(1)
    def set_start_time (self, time):
        self.start_time = time
        self.tot_time.append(time)
        self.curr_time = self.tot_time[0]
        self.set_start_time_delta()

    # Sets the truck object's start time to the provided time in a timedelta type: O(1)
    def set_start_time_delta(self):
        (h, m, s) = self.start_time.split(':')
        self.start_time_delta = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
