import csv
from Package import Package

class HashTable:

    # Hash Table constructor & fill: O(n)
    def __init__(self, file):
        self.file = file
        self.table = []
        self.capacity = self.get_list_len()
        for i in range(self.capacity):
            self.table.append([])
        self.fill_table()

    # Returns the hash of an item based on its key: O(1)
    def get_hash(self, key):
        return key % self.capacity

    # Adds an item to the hash table: O(1)
    def add(self, key, item):
        self.table[key] = item

    # Inserts a package item into the hash table: O(1)
    def insert(self, p_id, address, city, state, zipcode, deadline, mass, status, spec_notes):
        package = Package(p_id, address, city, state, zipcode, deadline, mass, status, spec_notes)
        key = self.get_hash(p_id)
        self.table[key] = package

    # Returns a package object from hash table based on package id: O(1)
    def lookup(self, p_id):
        key = self.get_hash(p_id)
        return self.table[key]

    # Fills the hash table with packages from csv file: O(n)
    def fill_table(self):
        with open(self.file, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                package = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], 'In House', row[7])
                key = self.get_hash(package.pack_id)
                self.add(key, package)

    # Returns the length of the file: O(1)
    def get_list_len(self):
        with open(self.file, 'r') as file:
            csvreader = csv.reader(file)
            return len(list(csvreader))