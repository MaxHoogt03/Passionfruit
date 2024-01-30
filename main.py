from code.classes import battery, district, house
import matplotlib.pyplot as plt
import json
from code.algorithms import more_random as mr, random_to_greedy as rtg, greedy as gr, hillclimber as hc, simulatedannealing as sc, battery_relocation as br, heuristic_hill as hh


def prompting():
    print("Welcome to Passionfruits Smartgrid Project.")
    print("Which algorithm or code would you like to run? Press the number you would like to run and hit enter.\n")
    print("1. Random")
    print("2. Random to greedy")
    print("3. Greedy")
    print("4. Random to hillclimber")
    print("5. Random to Simmulated Annealing")
    print("6. Random to Heuristic Hill\n")
    algorithm = int(input("Insert Here: "))
    print()
    district = int(input("Nice, which district do you want to run the algorithm on? Insert here: "))
    print()
    print("Would you like to reform the districts to connect houses to each other?")
    print("1. YES")
    print("2. NO\n")
    reform_choice = int(input("Type the number here: "))
    if reform_choice == 2:
        print("Okay and what costs would you like to see?\n")
        print("1. Own costs")
        print("2. Shared costs")
        cost_scheme = bool(int(input("Insert the number here: ")) - 1)
        print()
        return algorithm, district, reform_choice, cost_scheme
    return algorithm, district, reform_choice
    


def Printing_costs(reform_choice, costcategory = 3):
    with open("output.json", "r") as file:
        data = json.load(file)

    own_costs = data[0]["costs-own"]
    shared_costs = data[0]["costs-shared"]

    if costcategory == 1 and reform_choice == 2:
        print(f"Own Costs: {own_costs}")
    
    elif costcategory == 2:
        print(f"Shared Costs: {shared_costs}")

    elif reform_choice == 1:
        print(f"Reformed Shared Costs: {shared_costs}")
    
    
        



if __name__ == "__main__":
    choice_list = prompting()
    districts = [
        district.District(1, "data/district_1/district-1_"),
        district.District(2, "data/district_2/district-2_"),
        district.District(3, "data/district_3/district-3_")
    ]


    # --------------------------- Heatmap -------------------------
    # districts[0].heatmap(3)
    # districts[1].heatmap()
    # districts[2].heatmap()

    # --------------------------- Random --------------------------
    if choice_list[0] == 1: 
        solution_district = mr.Random_to_Random(districts[choice_list[1] - 1])
        solution_district.random_solution()
        if choice_list[2] == 1:
            solution_district.district.reform()  
        solution_district.district.plot_cables()

    # --------------------------- RandomGreedy --------------------------
    if choice_list[0] == 2:
        
        solution_district = rtg.RandomGreedy(districts[choice_list[1] - 1])
        solution_district.greedy_solution()

        if choice_list[2] == 2:
            solution_district.district.reform()

        solution_district.district.plot_cables()
        solution_district.district.output()


    # --------------------------- Greedy --------------------------
    if choice_list[0] == 3:
        
        print("No solution possible!")
        
        #gr = gr.Greedy(districts[choice_list[1] - 1])
        #gr.greedy_solution()

    # --------------------------- Random to Hillclimber -----------------------------
    if choice_list[0] == 4:
        solution_district = rtg.RandomGreedy(districts[choice_list[1] - 1])
        solution_district.greedy_solution()

        if len(choice_list) == 4:
            hillclimber_1 = hc.Hillclimber(solution_district.district, own_costs = choice_list[3])
        else:
            hillclimber_1 = hc.Hillclimber(solution_district.district, own_costs = False)

        sollution = hillclimber_1.run(5000, True)
        if choice_list[2] == 1:
            sollution.reform()
        sollution.plot_cables()
        sollution.output()

    # --------------------------- Random to Simulated Annealing ---------------------
    if choice_list[0] == 5:
        solution_district = rtg.RandomGreedy(districts[choice_list[1] - 1])
        solution_district.greedy_solution()

        if len(choice_list) == 4:
            sc_1 = sc.SimulatedAnnealing(solution_district.district, own_costs = choice_list[3])
        else:
            sc_1 = sc.SimulatedAnnealing(solution_district.district, own_costs = False)

        sollution = sc_1.run(10000, True)
        if choice_list[2] == 1:
            sollution.reform()
        sollution.plot_cables()
        sollution.output()

    # --------------------------- Random to Heuristic Hill ---------------------
    if choice_list[0] == 6:
        solution_district = rtg.RandomGreedy(districts[choice_list[1] - 1])
        solution_district.greedy_solution()

        if len(choice_list) == 4:
            sollution = heuristic_hill = hh.Heuristic_Hill(solution_district.district, own_costs = choice_list[3])
        else:
            sollution = heuristic_hill = hh.Heuristic_Hill(solution_district.district, own_costs = False)

        if choice_list[3] == 1:
            sollution.reform()
        sollution.plot_cables()
        sollution.output()
    
    if len(choice_list) == 3:
        Printing_costs(choice_list[2])
    else:
        Printing_costs(choice_list[2], choice_list[3])

