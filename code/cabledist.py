"""
Calculate closest battery for every single house and adding all distances to each other. It also adds the cables coordinates to the house object.
"""
import csv

from classes.house import House
from classes.battery import Battery
from classes.district import District

district_1 = District(1)

district_1_batteries = Battery.read_battery('../data/district_1/district-1_batteries.csv')
district_1_houses = House.read_house('../data/district_1/district-1_houses.csv')

def calculate_distance(point1, point2):
    return abs(point1.x - point2.x) + abs(point1.y - point2.y)

min_distance = None
min_distance_house = None
min_distance_battery = None
min_distance_per_house = None
total_min_distance = 0
test = 0
list_of_houses = []
list_of_batteries = []

for house in district_1_houses:
    for battery in district_1_batteries:
        distance = calculate_distance(house, battery)
        if min_distance is None or distance < min_distance:
            min_distance = distance
            min_distance_house = house
            min_distance_battery = battery

        if min_distance_per_house is None or distance < min_distance_per_house:
            min_distance_per_house = distance

    x_house = min_distance_house.x
    y_house = min_distance_house.y
    x_battery = min_distance_battery.x
    y_battery = min_distance_battery.y
    dist_x = x_house - x_battery
    dist_y = y_house - y_battery

    if dist_x < 0:
        for i in range(abs(dist_x)):
            min_distance_house.add_cable(f"{x_house + i}, {y_house}")
    
    elif dist_x > 0:
        for i in range(dist_x):
            min_distance_house.add_cable(f"{x_house-i}, {y_house}")

    if dist_y < 0:
        for i in range(abs(dist_y) + 1):
            min_distance_house.add_cable(f"{x_house - dist_x}, {y_house + i}")
    
    else:
        for i in range(dist_y + 1):
            min_distance_house.add_cable(f"{x_house-dist_x}, {y_house - i}")    


    total_min_distance += min_distance_per_house
    min_distance = None
    min_distance_per_house = None
    list_of_houses.append(min_distance_house)
    min_distance_battery.add_house(min_distance_house)
    list_of_batteries.append(min_distance_battery)

    

print(f"The minimum distance in district 1 is {min_distance} between {min_distance_house} and {min_distance_battery}")
print(total_min_distance)


for house in list_of_houses:
    district_1.add_house(house)

for battery in list_of_batteries:
    district_1.add_battery(battery)

print(district_1.output())