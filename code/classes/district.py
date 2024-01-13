import json
import csv
import matplotlib.pyplot as plt


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
    
    def calculate_distance(point1, point2):
        """
        Calculates the distance between Two points on an x,y plane By adding the x and y difference.
        
        pre: int
        post: int

        """
        return abs(point1.x - point2.x) + abs(point1.y - point2.y)


    def calculate_own_costs(self):
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

        return self.own_costs


    def get_houses(self):
        """
        returns the houses in the district.

        pre: none
        post: list of objects

        """

        return self.houses
    

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
        for house in self.houses:
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

        # Adjusting format of the plot.
        plt.xlabel('X Coordinate')
        plt.ylabel('Y Coordinate')
        plt.title('Cable Paths for All Houses')
        plt.grid(True)
        plt.savefig('plot.png')


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
                "own-costs": self.calculate_own_costs()
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
