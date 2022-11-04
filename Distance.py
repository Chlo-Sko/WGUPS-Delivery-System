import csv

class Distance:
    # Create list of addresses and names from CSV: O(1)
    with open("Resources/AddressNames.csv") as add_file:
        csv_add = csv.reader(add_file)
        csv_add = list(csv_add)

    # Create list of distances from CSV: O(1)
    with open("Resources/DistanceTable.csv") as dist_file:
        csv_dist = list(csv.reader(dist_file, delimiter=','))

        # Returns the distance between the previous location of a truck and its current location: O(1)
        def get_dist(self, curr_loc, prev_loc):
            row = int(curr_loc)
            col = int(prev_loc)
            dist = self.csv_dist[row][col]
            if dist is None or dist == '':
                dist = self.csv_dist[col][row]
            return float(dist)

        # Returns the integer location number based on its address: O(n)
        def get_loc_num(self, loc):
            for address in self.csv_add:
                if loc == address[2]:
                    return address[0]

        # Returns the total distance the truck has traveled: O(n)
        def get_tot_dist(self, truck):
            tot_dist = 0
            for t in truck:
                if truck[0] == t:
                    prev_loc = 0
                curr_loc = self.get_loc_num(t.get_address())
                dist = self.get_dist(curr_loc, prev_loc)
                prev_loc = curr_loc
                tot_dist += float(dist)
            dist = self.get_dist(curr_loc, 0)
            tot_dist += float(dist)
            return round(tot_dist, 2)