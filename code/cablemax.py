"""
Calculate furthest battery for every single house and adding all distances to each other.
"""
import csv

from classes.house import House
from classes.battery import Battery

district_1_batteries = Battery.read_battery('../data/district_1/district-1_batteries.csv')
district_1_houses = House.read_house('../data/district_1/district-1_houses.csv')

def calculate_distance(point1, point2):
    return abs(point1.x - point2.x) + abs(point1.y - point2.y)

largest_distance = 0
largest_distance_house = None
largest_distance_battery = None
max_distance = 0
total_max_distance = 0

for house in district_1_houses:
    for battery in district_1_batteries:
        distance = calculate_distance(house, battery)
        if distance > max_distance:
            max_distance = distance
            max_distance_house = house
            max_distance_battery = battery

        if distance > largest_distance:
            largest_distance = distance
            largest_distance_house = house
            largest_distance_battery = battery

    total_max_distance += max_distance
    max_distance = 0

print(f"The maximum distance in district 1 is {largest_distance} between {largest_distance_house} and {largest_distance_battery}")
print(total_max_distance)

    
