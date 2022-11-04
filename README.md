# WGUPS-Delivery-System
C950 - Data Structures and Algorithms II - Performance Assessment Truck Sorting Algorithm

Stated Problem:
The purpose of this project is to create an algorithm using Python 3.10 to assist Western Governors
University Parcel Service (WGUPS) in finding the optimal routes for delivery trucks given a list of
packages, their addresses, and additional criteria pertaining to each package. Due to a lack of consistency
in WGUPS’s ability to meet package delivery deadlines, this program is being implemented as a vital
solution to not only these issues, but many more, including optimizing mileage traveled (and therefore,
time spent) by each driver and truck. By utilizing this solution, WGUPS will see an increase in efficiency
and ability to meet deadlines and adapt swiftly to adjustments.

Programming Environment:
The program was written using Python 3.10 in the PyCharm Community Edition 2021.3 developing
environment on a Lenovo Flex laptop running Windows 10 Pro.

Algorithm Overview:
The routing function of the WGUPS delivery program utilizes both a greedy algorithm as well as nearest
neighbor algorithm to produce the most optimal route for each truck to deliver. The greedy algorithm
reads the package criteria and sorts the packages into trucks based on the best fit. Once the packages are
loaded onto their respective trucks, each package address is considered in order to find the nearest
deliverable address to the truck’s current location. This assessment is repeated at each stop to ensure the
truck travels the minimal amount of distance and therefore the minimal amount of time in order to meet
package delivery deadlines.
