from code.classes import district
import matplotlib.pyplot as plt
import json
from code.algorithms import more_random as mr, random_to_greedy as rtg, greedy as gr, hillclimber as hc, simulatedannealing as sc, battery_relocation as br, heuristic_hill as hh

district_1 = district.District(1, "data/district_1/district-1_")

total_min_distance = 0

for house in district_1.get_houses():
    smallest_distance = float('inf')
    for battery in district_1.get_batteries():
        distance = district.District.calculate_distance(house, battery)
        if distance < smallest_distance:
            smallest_distance = distance

    total_min_distance += smallest_distance

total_min_costs = total_min_distance*9 + 5000*5

print(f"Theoretical minimal costs: {total_min_costs}")