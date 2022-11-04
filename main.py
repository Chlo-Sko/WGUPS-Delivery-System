""" C950 Performance Assessment Written by Chloe Skorpikova - Student ID: 001128673 """

from HashTable import HashTable
from Truck import Truck
from Route import Route
from Distance import Distance

# The file from which to get package information
package_file = "Resources/PackageFile.csv"

# Constructs Route & Distance Class Objects to be used for distance calculations and route planning
route = Route()
distance = Distance()

# Creates an empty list for which to fill all packages
all_packages = []

# Takes all packages from hash table and adds them to a list to be iterated: O(n)
def create_package_list(package_table):
    i = 1
    while i <= package_table.get_list_len():
        package = package_table.lookup(i)
        all_packages.append(package)
        i += 1

# The initial greeting of the console interface: O(1)
def greeting():
    print('\n ----- Welcome to WGUPS Control System. -----')
    print('\nPlease, choose from the below options menu:')
    print('Get Truck Statuses: (t)')
    print('Get Package Statuses: (p)')
    print('Exit System: (e)')

# The prompt given to the user to navigate the console interface menu: O(n)
def prompt():
    user_input = ''
    while user_input != 'e':
        greeting()
        user_input = input('\nPlease, type letter corresponding with your preferred action: ')
        if user_input == 'p':
            route.get_package_statuses()
        if user_input == 't':
            print('\n--- Truck Statuses ---')
            for truck in trucks:
                print(truck)

    print('\n----- Thank you for visiting the WGUPS Control System. Goodbye. -----')

# Constructs Three Truck Class Objects and Sets Their Start Times: O(1)
truck1 = Truck(1)
truck2 = Truck(2)
truck3 = Truck(3)
truck1.set_start_time('8:00:00')
truck2.set_start_time('09:05:00')
truck3.set_start_time('10:20:00')

# A List of All Truck Class Objects for Iteration
trucks = [truck1, truck2, truck3]

# The main Program Run at Initiation, Creates the Hash Table, Route, Delivers Packages and Opens Console Interface: O(n)
if __name__ == '__main__':
    package_table = HashTable(package_file)
    create_package_list(package_table)
    route.run_route(all_packages, trucks)
    prompt()
