import csv

from models import Battery, House, read_battery, read_house

district_1_batteries = read_battery('district-1_batteries.csv')
district_1_houses = read_house('district-1_houses.csv')

def calculate_distance(point1, point2):
    return abs(point1.x - point2.x) + abs(point1.y - point2.y)

max_distance = 0
max_distance_house = None
max_distance_battery = None
total_max_distance = 0

for house in district_1_houses:
    max_distance_per_house = 0
    for battery in district_1_batteries:
        distance = calculate_distance(house, battery)
        if distance > max_distance:
            max_distance = distance
            max_distance_house = house
            max_distance_battery = battery

        if distance > max_distance_per_house:
            max_distance_per_house = distance

    total_max_distance += max_distance_per_house

print(f"The maximum distance in district 1 is {max_distance} between {max_distance_house} and {max_distance_battery}")
print(total_max_distance)