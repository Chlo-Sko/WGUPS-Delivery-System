import datetime

class Route:

    # Initializes a Route Object: O(1)
    def __init__(self):
        self.prioritized = []
        self.paired = []
        self.spec_truck = []
        self.delayed = []
        self.wrong_address = []
        self.standard = []
        self.en_route = []
        self.delivered = []
        self.all_packages = []

    # Sorts packages in the Route's packages list based on each package's criteria: O(n)
    def sort_packages(self):
        self.refresh_lists()
        for package in self.all_packages:
            if package.status == 'Delivered':
                self.delivered.append(package)
            elif package.status == 'En Route':
                self.en_route.append(package)
            elif package.is_delayed():
                self.delayed.append(package)
            elif package.is_paired() or package.get_id() == 13 or package.get_id() == 15 or package.get_id() ==19:
                self.paired.append(package)
            elif package.is_prioritized():
                self.prioritized.append(package)
            elif package.is_spec_truck():
                self.spec_truck.append(package)
            elif package.is_wrong_address():
                self.wrong_address.append(package)
            else:
                self.standard.append(package)

    # Loads a truck given by the truck parameter with packages in each of the lists based on their criteria: O(n)
    def load_truck(self, truck):
        if truck.t_id == 1:
            for p in self.paired:
                if not truck.is_full():
                    truck.load_package(p)
            for p in self.prioritized:
                if not truck.is_full():
                    truck.load_package(p)
            for p in self.standard:
                if not truck.is_full():
                    truck.load_package(p)
        elif truck.t_id == 2:
            for p in self.spec_truck:
                if not truck.is_full():
                    truck.load_package(p)
            for p in self.delayed:
                if not truck.is_full():
                    truck.load_package(p)
        else:
            for p in self.wrong_address:
                if not truck.is_full():
                    truck.load_package(p)
            for p in self.standard:
                truck.load_package(p)
        self.sort_packages()

    # Loads trucks based on a provided truck object list parameter: O(n)
    def load_trucks(self, trucks):
        for truck in trucks:
            self.load_truck(truck)

    # Unloads trucks based on a provided truck object list parameter: O(n)
    def unload_trucks(self, trucks):
        for truck in trucks:
            truck.unload_truck()

    # Combines three route functions to gather all packages, sort them into trucks and deliver them: O(n^2)
    def run_route(self, packages, trucks):
        self.get_all_packages(packages)
        self.load_trucks(trucks)
        self.unload_trucks(trucks)

    # Clears lists prior to sorting: O(1)
    def refresh_lists(self):
        self.prioritized = []
        self.paired = []
        self.spec_truck = []
        self.delayed = []
        self.wrong_address = []
        self.standard = []
        self.delivered = []

    # Retrieves packages from a given package_list and adds them to a local list, all_packages: O(1)
    def get_all_packages(self, package_list):
        for p in package_list:
            self.all_packages.append(p)
        self.sort_packages()

    # Prints package statuses based on provided timestamp: O(n)
    def get_package_statuses(self):
        time = input('Please input a time for status report in the format (XX:XX:XX): ')

        in_house = []
        loaded = []
        delivered = []
        for p in self.all_packages:
            (h, m, s) = time.split(':')
            d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            if p.delivery_time < d:
                delivered.append(p)
            elif p.load_time < d:
                loaded.append(p)
            else:
                in_house.append(p.get_id())
        print('\n---- Status of Packages at:', time, '----')
        print('\nIn House:', in_house)
        print('\nLoaded on Trucks:')
        for p in loaded:
            print('Package:', p.get_id(),'on Truck:',p.delivery_truck.t_id, '\t deadline:', p.get_deadline())
        print('\nDelivered:')
        for p in delivered:
            print(p)


