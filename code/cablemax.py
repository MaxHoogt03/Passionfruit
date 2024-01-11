"""
Calculate furthest battary for every single house and adding all distances to each other.
"""
import csv

from classes.house import House
from classes.battery import Battery

district_1_batteries = Battery.read_battery('../data/district_1/district-1_batteries.csv')
district_1_houses = House.read_house('../data/district_1/district-1_houses.csv')

def calculate_distance(point1, point2):
    return abs(point1.x - point2.x) + abs(point1.y - point2.y)

max_distance = 0
max_distance_house = None
max_distance_battery = None
max_distance_per_house = 0
total_max_distance = 0

for house in district_1_houses:
    for battery in district_1_batteries:
        distance = calculate_distance(house, battery)
        if distance > max_distance:
            max_distance = distance
            max_distance_house = house
            max_distance_battery = battery

        if distance > max_distance_per_house:
            max_distance_per_house = distance

    total_max_distance += max_distance_per_house
    max_distance_per_house = 0

print(f"The maximum distance in district 1 is {max_distance} between {max_distance_house} and {max_distance_battery}")
print(total_max_distance)

    
