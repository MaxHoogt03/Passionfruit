import json

class District:
    def __init__(self, value):
        self._value = value
        self.houses = []
        self.batteries = []
        self.own_costs = 0
        self.shared_costs = 0

    def add_house(self, house):
        self.houses.append(house)

    def add_battery(self, battery):
        self.batteries.append(battery)

    def calculate_own_costs(self):
        self.own_costs = 0
        for house in self.houses:
            self.own_costs += house.count_cables() * 9

        return self.own_costs

    def output(self):
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
                battery_info["houses"].append(house_info)

            data.append(battery_info)


        return json.dumps(data, indent = 2)
