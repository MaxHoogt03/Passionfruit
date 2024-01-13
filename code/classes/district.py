import json

class District:
    def __init__(self, value):
        self._value = value
        self.houses = []
        self.batteries = []
        self.own_costs = 0
        self.shared_costs = 0


    def add_house(self, house):
        """
        Adds the house to a list.

        pre: Object house
        post: none

        side-effects: appends to self.houses.
        """

        self.houses.append(house)


    def add_battery(self, battery):
        """
        Adds the battery to a list.

        pre: object battery
        post: none

        side-effects: appends to self.batteries.
        """

        self.batteries.append(battery)


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
