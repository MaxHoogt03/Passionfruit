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



for item in district_1_houses:
    print(item.__str__())

