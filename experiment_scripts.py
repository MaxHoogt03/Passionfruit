from code.classes import district
from code.algorithms import more_random as mr, random_to_greedy as rtg, greedy as gr, hillclimber as hc, simulatedannealing as sa, heuristic_hill as hh
from code.algorithms import advanced_6 as a6, genetic as gen
import csv
import time

# Change for different district
district_1 = district.District(1, "data/district_1/district-1_")



# Create name.csv in visualisation/presentation. Change name to wanted filename
csv_file_path = "visualisation/presentation/name.csv"

with open(csv_file_path, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["solution", "time"])

# Change for the amount of iterations you want to do
iterations = 1000

"""
Remove quotations for simulated annealing experiment

for i in range(iterations):
    # Record start time
    start_time = time.time()

    # Create RandomGreedy instance and obtain initial solution
    instance = rtg.RandomGreedy(district_1)
    initial_solution = instance.greedy_solution()

    instance = sa.SimulatedAnnealing(initial_solution)
    solution = instance.run(10000)


    # Record end time
    end_time = time.time()

    # Open CSV file for writing (or create if it doesn't exist)
    with open(csv_file_path, 'a', newline='') as csvfile:
        # Create CSV writer
        csv_writer = csv.writer(csvfile)

        # Write solution and time in a single row
        csv_writer.writerow([solution.calculate_own_costs(), end_time - start_time])

    print(f"Iteration {i+1}")

"""


"""
Remove quotations for hillclimber experiment

for i in range(iterations):
    # Record start time
    start_time = time.time()

    # Create RandomGreedy instance and obtain initial solution
    instance = rtg.RandomGreedy(district_1)
    initial_solution = instance.greedy_solution()

    instance = hc.Hillclimber(initial_solution)
    solution = instance.run(10000)


    # Record end time
    end_time = time.time()

    # Open CSV file for writing (or create if it doesn't exist)
    with open(csv_file_path, 'a', newline='') as csvfile:
        # Create CSV writer
        csv_writer = csv.writer(csvfile)

        # Write solution and time in a single row
        csv_writer.writerow([solution.calculate_own_costs(), end_time - start_time])

    print(f"Iteration {i+1}")

"""

"""
Remove quotations for random greedy experiment

for i in range(iterations):
    # Record start time
    start_time = time.time()

    instance = rtg.RandomGreedy(district_1)
    solution = instance.greedy_solution()

    # Record end time
    end_time = time.time()

    # Open CSV file for writing (or create if it doesn't exist)
    with open(csv_file_path, 'a', newline='') as csvfile:
        # Create CSV writer
        csv_writer = csv.writer(csvfile)

        # Write solution and time in a single row
        csv_writer.writerow([solution.calculate_own_costs(), end_time - start_time])

    print(f"Iteration {i+1}")
    
"""

"""
Remove quotations for random experiment

for i in range(iterations):
    # Record start time
    start_time = time.time()

    instance = mr.Random_to_Random(district_1)
    solution = instance.random_solution()

    # Record end time
    end_time = time.time()

    # Open CSV file for writing (or create if it doesn't exist)
    with open(csv_file_path, 'a', newline='') as csvfile:
        # Create CSV writer
        csv_writer = csv.writer(csvfile)

        # Write solution and time in a single row
        csv_writer.writerow([solution.calculate_own_costs(), end_time - start_time])

    print(f"Iteration {i+1}")

"""

