"""
Calculate closest battery for every single house and adding all distances to each other. It also adds the cables coordinates to the house object.
"""
import csv
import matplotlib.pyplot as plt
from classes.house import House
from classes.battery import Battery

district_1_batteries = Battery.read_battery('../data/district_1/district-1_batteries.csv')
district_1_houses = House.read_house('../data/district_1/district-1_houses.csv')

def calculate_distance(point1, point2):
    return abs(point1.x - point2.x) + abs(point1.y - point2.y)

smallest_distance = None
min_distance_house = None
min_distance_per_battery = None
min_distance = None
total_min_distance = 0
test = 0
list_of_houses = []

for house in district_1_houses:
    for battery in district_1_batteries:
        distance = calculate_distance(house, battery)
        if smallest_distance is None or distance < smallest_distance:
            smallest_distance = distance
            smallest_distance_house = house
            smallest_distance_battery = battery

        if min_distance is None or distance < min_distance:
            min_distance = distance
            min_distance_house = house
            min_distance_battery = battery

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
    
    elif dist_y > 0:
        for i in range(dist_y + 1):
            min_distance_house.add_cable(f"{x_house-dist_x}, {y_house - i}")    


    total_min_distance += min_distance
    min_distance = None
    list_of_houses.append(min_distance_house)


print(f"The minimum distance in district 1 is {smallest_distance} between {smallest_distance_house} and {smallest_distance_battery}")
print(total_min_distance)
print(smallest_distance_house.get_cables())


def plot_cables(houses):
    for house in houses:
        
        x_coords = []
        y_coords = []

        for coord in house.get_cables():
            x, y = coord.split(',')
            x_coords.append(int(x))
            y_coords.append(int(y))

        plt.plot(x_coords, y_coords, color='blue')

        plt.plot(x_coords[0], y_coords[0], marker='^', color='green', markersize=10)

        plt.plot(x_coords[-1], y_coords[-1], marker='s', color='red', markersize=10)
        
# Plotting for all houses
plot_cables(list_of_houses)

plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.title('Cable Paths for All Houses')
plt.grid(True)
plt.savefig('plot.png')