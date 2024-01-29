import json
import csv
import matplotlib.pyplot as plt
import random
from .house import House
from .battery import Battery

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
        # Reads the csv and adds the house objects to a list.
        with open(f"{path}houses.csv", 'r') as file:
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

        # Reads the csv, returns the batteries in a list.
        with open(f"{path}batteries.csv", 'r') as file:
            csv_reader = csv.DictReader(file)

            for row in csv_reader:
                x, y = row['positie'].split(',')
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
    
    def calculate_distance2(self,point1, point2):
        """
        Calculates the distance between Two points on an x,y plane By adding the x and y difference.
        
        pre: int
        post: int

        """
        return abs(point1.x - point2.x) + abs(point1.y - point2.y)

    def calculate_shared_costs(self, battery_costs = [5000, 5000, 5000, 5000, 5000]):
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
        self.shared_costs = 9*number_of_duplicates
        
        return int(self.calculate_own_costs(battery_costs)) - int(self.shared_costs)
    

    def calculate_own_costs(self, battery_costs = [5000, 5000, 5000, 5000, 5000]):
        """
        calculates the cost of laying the cables in the district and returns it.

        pre: none
        post: returns an int.
        
        side-effect: Adjusts the value of self.own_costs
        """

        # Set to zero to prevent adding multiple calls of this function to each other.
        self.own_costs = 0

        for house in self.houses:
            # Formula, since every cable is 9 dollars.
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

        x_to_find, y_to_find = original_house.x, original_house.y

        # Iterate through houses in the district and find the corresponding one
        for district_house in self.houses:
            if district_house.x == x_to_find and district_house.y == y_to_find:
                return district_house

        # Handle the case where the corresponding house is not found
        raise ValueError(f"Corresponding house not found for coordinates ({x_to_find}, {y_to_find})")
    
    def find_corresponding_battery(self, coordinates):
        """
        Tries to find a battery using coordinates
        
        pre: coordinates of battery
        post: house object or ValueError
        """

        # Split the string into x and y values
        x_str, y_str = coordinates.split(', ')

        # Convert the string values to integers
        x_to_find = int(x_str)
        y_to_find = int(y_str)

        for district_battery in self.batteries:
            if district_battery.x == x_to_find and district_battery.y == y_to_find:
                return district_battery
            
        # Handle the case where the corresponding house is not found
        raise ValueError(f"Corresponding battery not found for coordinates ({x_to_find}, {y_to_find})")
    

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

        colors = [
            '#7fbfde',  # light blue
            '#97d07d',  # light green
            '#fc8d8d',  # light red
            '#fecb67',  # light orange
            '#d1a3d9',  # light purple
        ]

        # Vibrant colors for the batteries
        vibrant_colors = [
            '#0077b3',  # vibrant blue
            '#2ca02c',  # vibrant green
            '#d62728',  # vibrant red
            '#ff7f0e',  # vibrant orange
            '#8c56b3',  # vibrant purple
        ]

        # Create a dictionary mapping battery coordinates to colors
        battery_color_map = {}
        for index, battery in enumerate(self.batteries):
            battery_coord = (battery.x, battery.y)
            battery_color_map[battery_coord] = colors[index]

        for house in self.houses:
            random_offset = random.uniform(-1, 1)

            x_coords = []
            y_coords = []

            # Converts coordinate strings to int and adds them to their list.
            for coord in house.get_cables():
                x, y = coord.split(',')
                x = int(x)
                y = int(y)
                if coord != house.get_cables()[-1]:
                    x = int(x) + random_offset  # Apply the random offset to x coordinate
                    y = int(y) + random_offset  # Apply the random offset to y coordinate
                x_coords.append(x)
                y_coords.append(y)

            # Get the color based on the last cable's coordinate (which is the battery's coordinate)
            last_cable_coord = (x_coords[-1], y_coords[-1])
            cable_and_house_color = battery_color_map.get(last_cable_coord, 'black')  # Default to black if not found

            # Plot the cables
            plt.plot(x_coords, y_coords, color=cable_and_house_color, linewidth=1)

            # Plots the houses
            plt.plot(x_coords[0], y_coords[0]+1, marker='^', color=cable_and_house_color, markersize=10)

        # Plot the batteries with vibrant colors
        for index, battery in enumerate(self.batteries):
            plt.plot(battery.x, battery.y, marker='s', color=vibrant_colors[index], markersize=10)

        plt.xlabel('X Coordinate')
        plt.ylabel('Y Coordinate')
        plt.title(f'Cable Paths for All Houses district {self._value}')
        plt.grid(True)
        plt.savefig(f'visualisation/gridcables/plot{self._value}.png')

    def heatmap(self, heatsize = 5):
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

        plt.hist2d(x, y, bins=(heatsize,heatsize))

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
        # Info on which district and the costs.
        data = [
            {
                "district": self._value,
                "costs-own": self.calculate_own_costs(),
                "costs-shared": self.calculate_shared_costs()
            },
        ]

        # Iterate over batteries and add their information to the data list
        for battery in self.batteries:
            battery_info = {
                "location": battery.get_location(),
                "capacity": battery.get_capacity(),
                "houses": []  # Placeholder for houses information
                # Add other battery information as needed
            }

            # Iterate over houses associated with the current battery
            for house in battery.get_houses():
                house_info = {
                    "location": house.get_location(),
                    "output": house.get_output(),
                    "cables": house.get_cables()
                }
                # houses was an empty list in the battery_info dictionary and we append here.
                battery_info["houses"].append(house_info)

            # data is a list of dictionaries and here we add another dictionary.
            data.append(battery_info)

        # Writing the json file.
        with open('output.json', 'w') as json_file:
            json.dump(data, json_file, indent=2)  # 'indent' for pretty formatting

        # returning the json as a string.
        return json.dumps(data, indent = 2)
    

    def reform(self):
        """
        This part of the code detects when houses which have the same connection to a battery, have cables which run parralel and 
        checks if its better to just connect these houses and adjusts this if necessary.
        """
        list_of_batteries = self.get_batteries()
        for battery in list_of_batteries:
            
            list_of_houses = battery.get_houses()
            battery_coordinates = battery.get_location()

            for idx, house in enumerate(list_of_houses):
                smallest_distance = self.calculate_distance2(house, battery)
                target_house = None
                for house2 in list_of_houses[idx + 1:]:
                    
                    if self.calculate_distance2(house, house2) < smallest_distance:
                        smallest_distance = self.calculate_distance2(house,house2)
                        target_house = house2
                

                if target_house is not None:
                    house.cables = []
                    x_house = house.x
                    y_house = house.y
                    x_target_house = target_house.x
                    y_target_house = target_house.y
                    dist_x = x_house - x_target_house
                    dist_y = y_house - y_target_house

                    # Adds the cables to the houses, by first walking over the x difference and then the y difference.
                    if dist_x <= 0:
                        for i in range(abs(dist_x)):
                            house.add_cable(f"{x_house + i}, {y_house}")

                    elif dist_x >= 0:
                        for i in range(dist_x):
                            house.add_cable(f"{x_house - i}, {y_house}")

                    if dist_y <= 0:
                        for i in range(abs(dist_y) + 1):
                            house.add_cable(f"{x_house - dist_x}, {y_house + i}")

                    elif dist_y >= 0:
                        for i in range(dist_y + 1):
                            house.add_cable(f"{x_house - dist_x}, {y_house - i}")
                
                else:
                    continue
                    
                

                     
                        
