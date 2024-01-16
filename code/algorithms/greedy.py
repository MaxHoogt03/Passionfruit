import random
import copy

from ..classes.district import District

def house_closest_to_battery(district):
    """
    Finds the house in a list which has the least Manhattan distance to a battery with enough capacity
    """
    def distance_to_battery(house, battery, district):
        """
        Calculates the distance from a house to a battery, considering battery capacity.
        Returns None if the house output exceeds the battery capacity.
        """
        if house.get_output() > battery.get_capacity():
            return None

        return district.calculate_distance(house, battery)

    houses = district.get_houses()
    batteries = district.get_batteries()

    closest_house = min(houses, key=lambda house: min(distance_to_battery(house, battery) for battery in batteries))

    return closest_house
