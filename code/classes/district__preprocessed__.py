# NOTE: This file was automatically generated from:
# /mnt/c/Users/stefa/Documents/algo&heur/Passionfruit/code/classes/district.py
# DO NOT CHANGE DIRECTLY! 1706806869.3160703
import json
import csv
import matplotlib.pyplot as plt
import random
try:
    (House,) = ultraimport('__dir__/house/__init__.py', objects_to_import=('House',), recurse=True)
except ultraimport.ResolveImportError as e:
    try:
        (House,) = ultraimport('__dir__/house.py', objects_to_import=('House',), recurse=True)
    except ultraimport.ResolveImportError as e2:
        raise ultraimport.RewrittenImportError(code_info=('from .house import House', '/mnt/c/Users/stefa/Documents/algo&heur/Passionfruit/code/classes/district.py', 5, 0), object_to_import='House', combine=[e, e2]) from None
try:
    (Battery,) = ultraimport('__dir__/battery/__init__.py', objects_to_import=('Battery',), recurse=True)
except ultraimport.ResolveImportError as e:
    try:
        (Battery,) = ultraimport('__dir__/battery.py', objects_to_import=('Battery',), recurse=True)
    except ultraimport.ResolveImportError as e2:
        raise ultraimport.RewrittenImportError(code_info=('from .battery import Battery', '/mnt/c/Users/stefa/Documents/algo&heur/Passionfruit/code/classes/district.py', 6, 0), object_to_import='Battery', combine=[e, e2]) from None

class District:

    def __init__(self, value, path):
        self._value = value
        self.houses = self.load_houses(path)
        self.batteries = self.load_batteries(path)
        self.own_costs = 0
        self.shared_costs = 0

    def load_houses(self, path):
        """
        Reads a csv file and returns a list of houses.

        pre: filename house data: str
        post: returns list of House objects.

        """
        house_list = []
        with open(f'{path}houses.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                x = row['x']
                y = row['y']
                maxoutput = row['maxoutput']
                house_list.append(House(x, y, maxoutput))
        return house_list

    def load_batteries(self, path):
        """
        Reads a csv file and returns a list of batteries.

        pre: filename battery data: str
        post: returns list of Battery objects.

        """
        battery_list = []
        with open(f'{path}batteries.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                (x, y) = row['positie'].split(',')
                capacity = row['capaciteit']
                battery_list.append(Battery(x, y, capacity))
        return battery_list

    def remove_batteries(self):
        """
        Clears self.battery_list
        """
        self.batteries.clear()

    def add_battery(self, x, y, capacity):
        """
        Adds battery to self.battery_list
        """
        self.batteries.append(Battery(x, y, capacity))

    def calculate_distance(point1, point2):
        """
        Calculates the distance between Two points on an x,y plane By adding the x and y difference.
        
        pre: int
        post: int

        """
        return abs(point1.x - point2.x) + abs(point1.y - point2.y)

    def calculate_distance2(self, point1, point2):
        """
        Calculates the distance between Two points on an x,y plane By adding the x and y difference.
        
        pre: int
        post: int

        """
        return abs(point1.x - point2.x) + abs(point1.y - point2.y)

    def calculate_shared_costs(self, battery_costs=[5000, 5000, 5000, 5000, 5000]):
        """
        calculates the total cost of laying the cables, but makes sure to account for the fact
        that houses can share a cable, so it subtracts the cables already laying there.
        
        pre: none
        post: returns an int

        side-effect: adjusts the value of self.shared_costs
        """
        self.shared_costs = 0
        cable_storedval = None
        number_of_duplicates = 0
        for battery in self.batteries:
            cable_dict = {}
            for house in battery.get_houses():
                cable_storedval = None
                for cable in house.get_cables():
                    if cable_storedval in cable_dict:
                        if cable_dict[cable_storedval] == cable:
                            number_of_duplicates += 1
                    elif cable_storedval is not None:
                        cable_dict[cable_storedval] = cable
                    cable_storedval = cable
        self.shared_costs = 9 * number_of_duplicates
        return int(self.calculate_own_costs(battery_costs)) - int(self.shared_costs)

    def calculate_own_costs(self, battery_costs=[5000, 5000, 5000, 5000, 5000]):
        """
        calculates the cost of laying the cables in the district and returns it.

        pre: none
        post: returns an int.
        
        side-effect: Adjusts the value of self.own_costs
        """
        self.own_costs = 0
        for house in self.houses:
            self.own_costs += house.count_cables() * 9
        for battery in battery_costs:
            self.own_costs += battery
        return self.own_costs

    def get_houses(self):
        """
        returns the houses in the district.

        pre: none
        post: list of objects

        """
        return self.houses

    def find_corresponding_house(self, original_house):
        """
        Tries to find a house using coordinates
        
        pre: house object
        post: house object or ValueError
        """
        (x_to_find, y_to_find) = (original_house.x, original_house.y)
        for district_house in self.houses:
            if district_house.x == x_to_find and district_house.y == y_to_find:
                return district_house
        raise ValueError(f'Corresponding house not found for coordinates ({x_to_find}, {y_to_find})')

    def find_corresponding_battery(self, coordinates):
        """
        Tries to find a battery using coordinates
        
        pre: coordinates of battery
        post: house object or ValueError
        """
        (x_str, y_str) = coordinates.split(', ')
        x_to_find = int(x_str)
        y_to_find = int(y_str)
        for district_battery in self.batteries:
            if district_battery.x == x_to_find and district_battery.y == y_to_find:
                return district_battery
        raise ValueError(f'Corresponding battery not found for coordinates ({x_to_find}, {y_to_find})')

    def get_batteries(self):
        """
        returns the batteries in the district.

        pre: none
        post: list of objects

        """
        return self.batteries

    def plot_cables(self):
        """
        Plots the cables, houses and batteries on a grid and stores them to plot.png.

        pre: None
        post: None
        """
        colors = ['#7fbfde', '#97d07d', '#fc8d8d', '#fecb67', '#d1a3d9']
        vibrant_colors = ['#0077b3', '#2ca02c', '#d62728', '#ff7f0e', '#8c56b3']
        for (index, battery) in enumerate(self.batteries):
            house_list = battery.get_houses()
            battery_color = colors[index]
            for house in house_list:
                random_offset = random.uniform(-1, 1)
                x_coords = []
                y_coords = []
                for coord in house.get_cables():
                    (x, y) = coord.split(',')
                    x = int(x)
                    y = int(y)
                    x_coords.append(x)
                    y_coords.append(y)
                plt.plot(x_coords, y_coords, color=battery_color, linewidth=1)
                plt.plot(x_coords[0], y_coords[0] + 1, marker='^', color=battery_color, markersize=10)
        for (index, battery) in enumerate(self.batteries):
            plt.plot(battery.x, battery.y, marker='s', color=vibrant_colors[index], markersize=10)
        plt.xlabel('X Coordinate')
        plt.ylabel('Y Coordinate')
        plt.title(f'Cable Paths for All Houses district {self._value}')
        plt.grid(True)
        plt.savefig(f'visualisation/gridcables/plot{self._value}.png')

    def heatmap(self, heatsize=5):
        """
        Creates a heatmap using the x and y coordinates of all the houses and stores them to heatmap.png

        pre: None
        post: None
        """
        x = []
        y = []
        for house in self.get_houses():
            x.append(house.x)
            y.append(house.y)
        plt.hist2d(x, y, bins=(heatsize, heatsize))
        plt.colorbar()
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title(f'Heatmap for district {self._value}')
        plt.savefig(f'visualisation/heatmaps/heatmap{self._value}.png')
        plt.clf()

    def output(self):
        """
        Generates the results of the distrinct into a json format.

        pre: none
        post: string

        """
        data = [{'district': self._value, 'costs-own': self.calculate_own_costs(), 'costs-shared': self.calculate_shared_costs()}]
        for battery in self.batteries:
            battery_info = {'location': battery.get_location(), 'capacity': battery.capacity_output(), 'houses': []}
            for house in battery.get_houses():
                house_info = {'location': house.get_location(), 'output': house.get_output(), 'cables': house.get_cables()}
                battery_info['houses'].append(house_info)
            data.append(battery_info)
        with open('output.json', 'w') as json_file:
            json.dump(data, json_file, indent=2)
        return json.dumps(data, indent=2)

    def reform(self):
        """
        This part of the code detects when houses which have the same connection to a battery, have cables which run parralel and 
        checks if its better to just connect these houses and adjusts this if necessary.
        """
        list_of_batteries = self.get_batteries()
        for battery in list_of_batteries:
            list_of_houses = battery.get_houses()
            battery_coordinates = battery.get_location()
            for (idx, house) in enumerate(list_of_houses):
                smallest_distance = self.calculate_distance2(house, battery)
                target_house = None
                for house2 in list_of_houses[idx + 1:]:
                    if self.calculate_distance2(house, house2) < smallest_distance:
                        smallest_distance = self.calculate_distance2(house, house2)
                        target_house = house2
                if target_house is not None:
                    house.cables = []
                    x_house = house.x
                    y_house = house.y
                    x_target_house = target_house.x
                    y_target_house = target_house.y
                    dist_x = x_house - x_target_house
                    dist_y = y_house - y_target_house
                    if dist_x <= 0:
                        for i in range(abs(dist_x)):
                            house.add_cable(f'{x_house + i},{y_house}')
                    elif dist_x >= 0:
                        for i in range(dist_x):
                            house.add_cable(f'{x_house - i},{y_house}')
                    if dist_y <= 0:
                        for i in range(abs(dist_y) + 1):
                            house.add_cable(f'{x_house - dist_x},{y_house + i}')
                    elif dist_y >= 0:
                        for i in range(dist_y + 1):
                            house.add_cable(f'{x_house - dist_x},{y_house - i}')
                else:
                    continue