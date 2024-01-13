"""
Calculate closest battery for every single house and adding all distances to each other. It also adds the cables coordinates to the house object.
and prints the cables of the house with the smallest distance to a battery.
"""
import csv
import matplotlib.pyplot as plt
from classes.house import House
from classes.battery import Battery
from classes.district import District

# Initializing our objects.
district_1 = District(1, f'../data/district_1/district-1_')


def calculate_distance(point1, point2):
    """
    Calculates the distance between Two points on an x,y plane By adding the x and y difference.
    
    pre: int
    post: int

    """
    return abs(point1.x - point2.x) + abs(point1.y - point2.y)


# Variable to keep track of total distance of all seperate house-battery combinations.
total_min_distance = 0

# Loops over all houses and stores houses in 1 of the 5 battery object, which the house is closest to. 
for house in district_1.houses:
    smallest_distance = None

    # loops over all batteries and checks which battery is closest to current house, with its distance.
    for battery in district_1.batteries:
        distance = calculate_distance(house, battery)

        if smallest_distance is None or distance < smallest_distance:
            smallest_distance = distance
            closest_battery = battery

    # Variables for location of current house, closest battery and the distance.
    x_house = house.x
    y_house = house.y
    x_battery = closest_battery.x
    y_battery = closest_battery.y
    dist_x = x_house - x_battery
    dist_y = y_house - y_battery

    # Adds the cables to the houses, by first walking over the x difference and then the y difference.
    if dist_x < 0:
        for i in range(abs(dist_x)):
            house.add_cable(f"{x_house + i}, {y_house}")
    
    elif dist_x > 0:
        for i in range(dist_x):
            house.add_cable(f"{x_house-i}, {y_house}")

    if dist_y < 0:
        for i in range(abs(dist_y) + 1):
            house.add_cable(f"{x_house - dist_x}, {y_house + i}")
    
    elif dist_y > 0:
        for i in range(dist_y + 1):
            house.add_cable(f"{x_house-dist_x}, {y_house - i}")

    # Adds all distances of the houses to their closest battery.
    total_min_distance += smallest_distance

    # Adds to house to the current battery object.
    closest_battery.add_house(house)

    
# returns the "Sollution" into output.json
district_1.output()

# Finds the house with the shortest distance to a battery
cable_len = None
for house in district_1.get_houses():
    if cable_len is None or cable_len > house.count_cables():
        cable_len = house.count_cables()
        smallest_distance_house = house

# Finds the battery to which the house in the previous for loop is closest to.
for battery in district_1.get_batteries():
    if smallest_distance_house in battery.get_houses():
        closest_battery = battery


print(f"The minimum distance in district 1 is {smallest_distance_house.count_cables()} between {smallest_distance_house} and {closest_battery}")

# Prints the total distances of all houses to their batteries added together.
print(total_min_distance)

# Prints the cable Coordinates.
print(smallest_distance_house.get_cables())


def plot_cables(houses):
    """
    Plots the cables, houses and batteries on a grid and stores them to plot.png.

    pre: house object
    post: None
    """
    for house in houses:
        
        # Need to store the coordinates in lists, since they are stored as strings.
        x_coords = []
        y_coords = []

        # Converts coordinate strings to int and adds them to their list.
        for coord in house.get_cables():
            x, y = coord.split(',')
            x_coords.append(int(x))
            y_coords.append(int(y))

        # Plot the Lines
        plt.plot(x_coords, y_coords, color='blue')

        # Plots the houses (The fist cable can be used for location of the house since the cable starts at the house.)
        plt.plot(x_coords[0], y_coords[0], marker='^', color='green', markersize=10)

        # Plots the batteries (Same logic as above.)
        plt.plot(x_coords[-1], y_coords[-1], marker='s', color='red', markersize=10)
        
# Plotting for all houses
plot_cables(district_1.houses)

# Adjusting format of the plot.
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.title('Cable Paths for All Houses')
plt.grid(True)
plt.savefig('plot.png')
