# NOTE: This file was automatically generated from:
# /mnt/c/Users/Max/Downloads/Passionfruit/visualisation/presentation/theoretical_optimum.py
# DO NOT CHANGE DIRECTLY! 1706729063.0953724
import matplotlib.pyplot as plt
import sys
import os
import ultraimport
District = ultraimport('__dir__/../../code/classes/district.py', 'District', recurse=True)

def theoretical_optimum():
    """
    Calculates theoretical optimum own costs by simply taking the short Manhattan distance between all houses and batteries without the battery capacity constraints.
    """
    total_min_distance = 0
    district_1 = District(1, '../../data/district_1/district-1_')
    for house in district_1.get_houses():
        smallest_distance = float('inf')
        for battery in district_1.get_batteries():
            distance = District.calculate_distance(house, battery)
            if distance < smallest_distance:
                smallest_distance = distance
        total_min_distance += smallest_distance
    total_min_costs = total_min_distance * 9 + 5000 * 5
    return total_min_costs
print(f'Theoretical minimal costs: {theoretical_optimum()}')