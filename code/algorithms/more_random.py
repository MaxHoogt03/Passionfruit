import random
import copy

from ..classes.district import District

class Random_to_Random:
    def __init__(self, district):
        self.district = copy.deepcopy(district)
        self.random_solution()
        
    def add_cables(self, house, battery):
        """
        Adds cable coordinates from the house to the battery.
        """
        dist_x, dist_y = house.x - battery.x, house.y - battery.y

        # Walking over the x and y differences
        if dist_x <= 0:
            for i in range(abs(dist_x)):
                house.add_cable(f"{house.x + i},{house.y}")
        elif dist_x >= 0:
            for i in range(dist_x):
                house.add_cable(f"{house.x - i},{house.y}")

        if dist_y <= 0:
            for i in range(abs(dist_y) + 1):
                house.add_cable(f"{house.x - dist_x},{house.y + i}")
        elif dist_y >= 0:
            for i in range(dist_y + 1):
                house.add_cable(f"{house.x - dist_x},{house.y - i}")

    def find_valid_battery(self, house, battery):
        """
        Tries to find a battery which is valid for the given house.
        """
        
        for battery in self.district_copy.batteries:
            if battery.get_capacity() >= house.get_output():
                distance = District.calculate_distance(house, battery)
                return battery, distance
        return None, None

    def random_solution(self):
        """
        Generates a random solution for connecting houses to batteries.
        """
        retry = True
        while retry:
            self.district_copy = copy.deepcopy(self.district)
            random.shuffle(self.district_copy.houses)
            total_min_distance = 0
            retry = False  # Reset the retry flag at the beginning of each attempt

            for house in self.district_copy.houses:
                random.shuffle(self.district_copy.batteries)
                battery, distance = self.find_valid_battery(house, self.district_copy.batteries)

                if battery is not None and distance is not None:
                    # Adds the cables to the houses, by first walking over the x difference and then the y difference.
                    self.add_cables(house, battery)

                    # Adds all distances of the houses to their closest battery.
                    total_min_distance += distance

                    # Adds to house to the current battery object.
                    battery.add_house(house)
                else:
                    # If no suitable battery is found for a house, set the retry flag and break the loop
                    retry = True
                    break
                
        return self.district_copy