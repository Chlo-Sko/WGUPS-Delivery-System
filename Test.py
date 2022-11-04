from Distance import Distance
from Route import Route

distance = Distance()
route = Route()

def iterate_hash_table(package_table):
    i = 1

    while i < package_table.get_list_len() + 1:
        package = package_table.lookup(i)
        print(package)
        i += 1


def load_truck(package_table, truck):
    i = 1

    while not truck.is_full() and i <= package_table.get_list_len():
        package = package_table.lookup(i)
        if package.status == 'In House':
            truck.load_package(package)
            #print('Truck',truck.t_id,'Loaded Package', package.get_id())
        i += 1

def load_all_trucks(package_table, trucks):
    for truck in trucks:
        load_truck(package_table, truck)

def unload_all_trucks(trucks):
    for truck in trucks:
        truck.unload_truck()

def print_trucks(trucks):
    for truck in trucks:
        print(truck)

def print_package_locations(package_table):
    i = 1
    while i <= package_table.get_list_len():
        package = package_table.lookup(i)
        print('Package', package.get_id(), 'address: ', package.get_address(), '- Location:', distance.get_loc_num(package.get_address()))
        i += 1

def print_package_distances(package_table):
    i = 1
    while i <= package_table.get_list_len():
        package = package_table.lookup(i)
        address = package.get_address()
        curr_loc = distance.get_loc_num(address)
        print('Package',  package.get_id(),'location', curr_loc, 'distance from hub:', distance.get_dist(0, curr_loc))
        i += 1

def print_package_notes(package_table):
    i = 1
    while i <= package_table.get_list_len():
        package = package_table.lookup(i)
        notes = package.get_spec_notes()
        if notes > '':
            print('Package', package.get_id(), 'Notes:', notes, 'Prioritized:', package.is_prioritized())

        i += 1