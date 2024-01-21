"""
Calculate closest battery for every single house and adding all distances to each other. It also adds the cables coordinates to the house object.
and prints the cables of the house with the smallest distance to a battery.
"""
import csv
from classes.house import House
from classes.battery import Battery
from classes.district import District

# Initializing our objects.
district_0 = District(0, f'../data/district_0/district-0_')


houselist = district_0.get_houses()
list_of_batteries = district_0.get_batteries()

list_of_batteries[2].add_house(houselist[0])
houselist[0].add_cable("0, 5")
for i in range(1,6):
    houselist[0].add_cable(f"{0+i}, {5 - i + 1}")
    houselist[0].add_cable(f"{0+i}, {5-i}")

list_of_batteries[1].add_house(houselist[1])
houselist[1].add_cable("0, 0")
for i in range(1,6):
    houselist[1].add_cable(f"{0+i}, {0 + i - 1}")
    houselist[1].add_cable(f"{0+i}, {0 + i}")

list_of_batteries[0].add_house(houselist[2])
houselist[2].add_cable("0, 3")
for i in range(1,6):
    houselist[2].add_cable(f"{i}, 3")

list_of_batteries[0].add_house(houselist[3])
houselist[3].add_cable("1, 3")
for i in range(2,6):
    houselist[3].add_cable(f"{i}, 3")

for i in range(0,4):
    print(houselist[i].get_cables())
        
# Plotting for all houses
print(district_0.calculate_shared_costs())


