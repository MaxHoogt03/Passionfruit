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

houselist[0].add_cable("0, 5")
for i in range(1,6):
    houselist[0].add_cable(f"{0+i}, {5 - i + 1}")
    houselist[0].add_cable(f"{0+i}, {5-i}")

houselist[1].add_cable("0, 0")
for i in range(1,6):
    houselist[1].add_cable(f"{0+i}, {0 + i - 1}")
    houselist[1].add_cable(f"{0+i}, {0 + i}")

houselist[2].add_cable("0, 3")
for i in range(1,6):
    houselist[2].add_cable(f"{i}, 3")

for i in range(0,3):
    print(houselist[i].get_cables())
        
# Plotting for all houses
district_0.plot_cables()

print(district_0.calculate_shared_costs())


