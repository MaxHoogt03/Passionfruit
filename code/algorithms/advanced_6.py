import random
import copy

class Advanced_6:
    def __init__(self, district):
        self.district = copy.deepcopy(district)
        self.battery_data = {
            'PowerStar': {'capacity': 450, 'price': 900},
            'Imerse-II': {'capacity': 900, 'price': 1350},
            'Imerse-III': {'capacity': 1800, 'price': 1800}
        }

    def random_battery_list(self, needed_capacity):
        """
        Chooses enough random batteries from the battery_data to accommodate for the outputs from all houses in the district
        """

        battery_dict = {}
        capacity = 0
        price = 0

        i = 0

        while capacity < needed_capacity:
            i += 1

            random_name = random.choice(list(self.battery_data.keys()))
            random_capacity = self.battery_data[random_name]['capacity']
            random_price = self.battery_data[random_name]['price']

            capacity += random_capacity
            price += random_price
            battery_dict[f"{i}: {random_name}"] = {'capacity': random_capacity, 'price': random_price}
        
        return battery_dict, capacity, price
