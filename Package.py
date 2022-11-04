class Package:
    def __init__(self, pack_id, address, city, state, zipcode, deadline, mass, status, spec_notes):
        # Constructs a package object
        self.pack_id = int(pack_id)
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.mass = mass
        self.deadline = deadline
        self.status = status
        self.spec_notes = spec_notes

        self.delivery_truck = 0

        self.load_time = []
        self.delivery_time = []

    # Prints package object information to string: O(1)
    def __str__(self):
        return f'Package Id: {self.pack_id:02d}, Truck: {self.delivery_truck.t_id}, \t Deadline: {self.deadline}, \t Delivery Time: {self.delivery_time}'

    # Package getters

    # Retrieves package id: O(1)
    def get_id(self):
        return self.pack_id

    # Retrieves package address: O(1)
    def get_address(self):
        return self.address

    # Retrieves package status: O(1)
    def get_status(self):
        return self.status

    # Retrieves special notes: O(1)
    def get_spec_notes(self):
        return self.spec_notes

    # Retrieves deadline: O(1)
    def get_deadline(self):
        return self.deadline


    # Package setters

    # Sets package status: O(1)
    def set_status(self, status):
        self.status = status

    # Sets package address: O(1)
    def set_address(self, address, zipcode):
        self.address = address
        self.zipcode = zipcode


    # Package booleans:

    # Returns True if package is prioritized: O(1)
    def is_prioritized(self):
        return self.deadline != 'EOD'

    # Sets status to 'Awaiting' and returns True if package is delayed: O(1)
    def is_delayed(self):
        if 'Delayed' in self.spec_notes:
            self.set_status('Awaiting')
            return True
        return False

    # Returns True if package is paired with another: O(1)
    def is_paired(self):
        return 'Must be delivered with' in self.spec_notes

    # Returns True if package has wrong address: O(1)
    def is_wrong_address(self):
        return 'Wrong address' in self.spec_notes

    # Package Methods

    # Returns whether package needs to be delivered on a specific truck: O(1)
    def is_spec_truck(self):
        if 'Can only be on truck' in self.spec_notes:
            return True
        else:
            return False

    # Adds package to truck inventory, notes package load time and sets status to 'En Route': O(1)
    def load(self, truck):
        self.status = 'En Route'
        self.delivery_truck = truck
        self.load_time = truck.start_time_delta

    # Sets Package status to 'Delivered' and notes delivery time on the package object: O(1)
    def deliver(self, truck):
        self.status  = 'Delivered'
        self.delivery_time = truck.sum_time
