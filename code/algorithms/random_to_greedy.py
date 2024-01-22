import random
import copy

from ..classes.district import District

class RandomGreedy:

    def __init__(self, district):
        self.district = copy.deepcopy(district)

    def randomize_houses(self, district):
        """
        Randomly shuffles the list of houses from the given district
        """
        random.shuffle(district.get_houses())

    def add_greedy_connection(self, house, battery):
        """
        Adds the cables by first clearing the x difference between the house and battery and then y.
        """
        x_house = house.x
        y_house = house.y
        x_battery = battery.x
        y_battery = battery.y
        dist_x = x_house - x_battery
        dist_y = y_house - y_battery

        # Adds the cables to the houses, by first walking over the x difference and then the y difference.
        if dist_x < 0:
            for i in range(abs(dist_x)):
                house.add_cable(f"{x_house + i}, {y_house}")

        elif dist_x > 0:
            for i in range(dist_x):
                house.add_cable(f"{x_house - i}, {y_house}")

        if dist_y < 0:
            for i in range(abs(dist_y) + 1):
                house.add_cable(f"{x_house - dist_x}, {y_house + i}")

        elif dist_y > 0:
            for i in range(dist_y + 1):
                house.add_cable(f"{x_house - dist_x}, {y_house - i}")

    def greedy_solution(self):
        """
        Finds a greedy solution after random order of houses
        """
        retry = True
        while retry:
            district_copy = copy.deepcopy(self.district)
            self.randomize_houses(district_copy)

            total_min_distance = 0
            retry = False  # Reset the retry flag at the beginning of each attempt
            for house in district_copy.houses:
                smallest_distance = None
                closest_battery = None

                # loops over all batteries and checks which battery is closest to the current house, with its distance.
                for battery in district_copy.batteries:
                    distance = District.calculate_distance(house, battery)

                    if (smallest_distance is None or distance < smallest_distance) and battery.get_capacity() >= house.get_output():
                        smallest_distance = distance
                        closest_battery = battery

                if closest_battery is not None:
                    self.add_greedy_connection(house, closest_battery)

                    total_min_distance += smallest_distance
                    closest_battery.add_house(house)

                else:
                    # If no suitable battery is found for a house, set the retry flag and break the loop
                    retry = True
                    break
        
        self.district = district_copy
        
        return district_copy
