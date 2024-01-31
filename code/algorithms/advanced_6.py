import random
import copy

class Advanced_6:
    def __init__(self, district):
        """
        Initializes the Advanced_6 class by deep copying the provided district 
        and removing existing batteries. Sets up battery data and costs.

        
        pre: district (object)

        Side-effects:
        - Initializes class variables.
        """
        self.district = copy.deepcopy(district)
        self.district.remove_batteries()
        self.battery_data = {
            'PowerStar': {'capacity': 450, 'price': 900},
            'Imerse-II': {'capacity': 900, 'price': 1350},
            'Imerse-III': {'capacity': 1800, 'price': 1800}
        }
        self.battery_costs = []

    def random_battery_list(self, needed_capacity):
        """
        Chooses enough random batteries from the battery_data to accommodate 
        for the outputs from all houses in the district.

        
        pre: needed_capacity (int) 
        post: dict

        """
        battery_dict = {}
        capacity = 0
        i = 0

        while capacity < needed_capacity:
            i += 1
            random_name = random.choice(list(self.battery_data.keys()))
            random_capacity = self.battery_data[random_name]['capacity']
            random_price = self.battery_data[random_name]['price']

            capacity += random_capacity
            self.battery_costs.append(random_price)
            battery_dict[f"{i}: {random_name}"] = {'capacity': random_capacity, 'price': random_price}
        
        return battery_dict

    def add_batteries_to_district(self, battery_dict):
        """
        Places the given batteries at random locations on the district where 
        there are no other houses or batteries.

        
        pre: battery_dict (dict) 

        side-effects: Adds batteries to district.
        """
        max_attempts = 100

        for battery in battery_dict.values():
            capacity = battery['capacity']

            for _ in range(max_attempts):
                x, y = random.randint(0, 50), random.randint(0, 50)

                # Check for existing houses or batteries at the coordinates
                if any(house.x == x and house.y == y for house in self.district.get_houses()) or \
                   any(bat.x == x and bat.y == y for bat in self.district.get_batteries()):
                    continue

                # If no house or battery at the coordinates, add the battery and break out of the loop
                self.district.add_battery(x, y, capacity)
                break


    def run(self, needed_capacity):
        """
        Runs the algorithm to randomly select and place batteries in the district.

        
        pre: needed_capacity
        
        """
        batteries = self.random_battery_list(needed_capacity)
        self.add_batteries_to_district(batteries)

        for battery in self.district.get_batteries():
            print(battery)
