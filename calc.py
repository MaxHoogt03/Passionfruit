import csv

from models import Battery, House

district_1_batteries = []
district_1_houses = []

with open('data/district_1/district-1_batteries.csv', 'r') as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        x, y = row['positie'].split(',')
        capacity = row['capaciteit']
        district_1_batteries.append(Battery(x, y, capacity))

with open('data/district_1/district-1_houses.csv', 'r') as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        x = row['x']
        y = row['y']
        maxoutput = row['maxoutput']
        district_1_houses.append(House(x, y, maxoutput))


def calculate_distance(point1, point2):
    return abs(point1.x - point2.x) + abs(point1.y - point2.y)

max_distance = 0
max_distance_house = None
max_distance_battery = None

for house in district_1_houses:
    for battery in district_1_batteries:
        distance = calculate_distance(house, battery)
        if distance > max_distance:
            max_distance = distance
            max_distance_house = house
            max_distance_battery = battery

print(f"The maximum distance in district 1 is {max_distance} between {max_distance_house} and {max_distance_battery}")