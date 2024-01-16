import random
import copy

from ..classes.district import District

def house_closest_to_battery(district):
    """
    Finds the house in a list which has the least Manhattan distance to a battery with enough capacity.
    Removes the closest house and its corresponding battery from their respective lists.

    Args:
        district (District): The district containing houses and batteries.

    Returns:
        tuple: A tuple containing the closest house and its corresponding battery.
    """
    def distance_to_battery(house, battery):
        if house.get_output() > battery.get_capacity():
            return float('inf')  # Return a large value for invalid distances
        return district.calculate_distance(house, battery)

    houses = district.get_houses()
    batteries = district.get_batteries()

    min_distance = float('inf')
    closest_house = None
    closest_battery = None

    for house in houses:
        for battery in batteries:
            distance = distance_to_battery(house, battery)
            if distance < min_distance:
                min_distance = distance
                closest_house = house
                closest_battery = battery

    if closest_house and closest_battery:
        houses.remove(closest_house)

    return closest_house, closest_battery



def greedy_solution(district):
    district_copy = copy.deepcopy(district)
    while district_copy.get_houses():
        house, battery = house_closest_to_battery(district)
        