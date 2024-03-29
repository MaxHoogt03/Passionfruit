import random
import copy

from ..classes.district import District

class Greedy:
    def __init__(self, district):
        self.district = copy.deepcopy(district)

    def house_closest_to_battery(self, district, connected_houses):
        """
        Finds the house in a list which has the least Manhattan distance to a battery with enough capacity.
        Removes the closest house and its corresponding battery from their respective lists.

        Args:
            district (District): The district containing houses and batteries.
            connection_houses: set of already connected houses

        Returns:
            tuple: A tuple containing the closest house, its corresponding battery, and the minimum distance.
        """

        def distance_to_battery(house, battery):
            """
            Calculates the distance between a given house and battery.
            """

            if house.get_output() > battery.get_capacity():
                return float('inf')  # Return a large value for invalid distances
            return District.calculate_distance(house, battery)

        houses = district.get_houses()
        batteries = district.get_batteries()

        min_distance = float('inf')
        closest_house = None
        closest_battery = None

        for house in houses:
            if house in connected_houses:
                continue

            for battery in batteries:
                distance = distance_to_battery(house, battery)
                if distance < min_distance:
                    min_distance = distance
                    closest_house = house
                    closest_battery = battery

        if closest_house:
            connected_houses.add(closest_house)

        return closest_house, closest_battery, min_distance



    def greedy_solution(self):
        """
        Gives the greedy solution.
        """

        district_copy = copy.deepcopy(self.district)
        connected_houses = set()
        total_min_distance = 0

        houses_connected = 0

        while houses_connected < 150:
            house, battery, min_distance = self.house_closest_to_battery(district_copy, connected_houses)
            # Variables for location of current house, closest battery, and the distance.
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
                    house.add_cable(f"{x_house-i}, {y_house}")

            if dist_y < 0:
                for i in range(abs(dist_y) + 1):
                    house.add_cable(f"{x_house - dist_x}, {y_house + i}")
                    
            elif dist_y > 0:
                for i in range(dist_y + 1):
                    house.add_cable(f"{x_house-dist_x}, {y_house - i}")

            # Adds all distances of the houses to their closest battery.
            total_min_distance += min_distance

            # Adds to house to the current battery object.
            battery.add_house(house)
            houses_connected += 1

        return district_copy
