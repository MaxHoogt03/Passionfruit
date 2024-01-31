import matplotlib.pyplot as plt
import sys
import os
import ultraimport
District = ultraimport('__dir__/../../code/classes/district.py', 'District', recurse=True)

def theoretical_optimum(district):
    """
    Calculates theoretical optimum own costs by simply taking the short Manhattan distance between all houses and batteries without the battery capacity constraints.
    """

    total_min_distance = 0

    for house in district.get_houses():
        smallest_distance = float('inf')
        for battery in district.get_batteries():
            distance = District.calculate_distance(house, battery)
            if distance < smallest_distance:
                smallest_distance = distance

        total_min_distance += smallest_distance

    total_min_costs = total_min_distance * 9 + 5000 * 5
    return total_min_costs

district_1 = District(1, "../../data/district_1/district-1_")

print(f"Theoretical minimal costs: {theoretical_optimum(district_1)}")
