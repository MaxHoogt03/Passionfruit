from code.classes import battery, district, house
import matplotlib.pyplot as plt
from code.algorithms import more_random as mr, random_to_greedy as rtg, greedy as gr, hillclimber as hc, simulatedannealing as sc, battery_relocation as br, iterative as itr


def prompting():
    print("Welcome to Passionfruits Smartgrid Project.")
    print("Which algorithm or code would you like to run? Press the number you would like to run and hit enter.")
    print("1. Random")
    print("2. Random to greedy")
    print("3. Greedy")
    print("4. Random to hillclimber")
    print("5. Random to Simmulated Annealing")
    print("6. Random to Iterative")
    algorithm = int(input("Insert Here: "))
    district = int(input("Nice, which district do you want to run the algorithm on? Insert here: "))
    return algorithm, district






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
        data = mr.Random_to_Random(districts[choice_list[1] - 1])
        data.random_solution()
        data.district.plot_cables()
        
        #Histogram to see how the random cable length is distributed
        # results = []
        # for i in range(0):
        #     result = data.random_solution()
        #     results.append(result)
        # plt.hist(results, bins=20)
        # plt.title('Histogram of Results')
        # plt.xlabel('Result Value')
        # plt.ylabel('Frequency')
        # plt.savefig('plot.png')

    # --------------------------- Random to Greedy --------------------------
    if choice_list[0] == 2:
        
        random_solution_district = rtg.RandomGreedy(districts[choice_list[1] - 1])
        random_solution_district.greedy_solution()
        random_solution_district.district.plot_cables()
        random_solution_district.district.output()
    # --------------------------- Greedy --------------------------
    if choice_list[0] == 3:
        gr = gr.Greedy(districts[choice_list[1] - 1])
        gr.greedy_solution()

    # --------------------------- Random to Hillclimber -----------------------------
    if choice_list[0] == 4:
        random_solution_district = rtg.RandomGreedy(districts[choice_list[1] - 1])
        random_solution_district.greedy_solution()
        hillclimber_1 = hc.Hillclimber(random_solution_district.district, False)
        hillclimber_1.run(10000, True)

    # --------------------------- Random to Simulated Annealing ---------------------
    if choice_list[0] == 5:
        random_solution_district = rtg.RandomGreedy(districts[choice_list[1] - 1])
        random_solution_district.greedy_solution()
        sc_1 = sc.SimulatedAnnealing(random_solution_district.district, own_costs = True)
        sc_1.run(2000, True)

    # --------------------------- Random to Iterative ---------------------
    if choice_list[0] == 6:
        random_solution_district = rtg.RandomGreedy(districts[choice_list[1] - 1])
        random_solution_district.greedy_solution()
        iterative = itr.Iterative(random_solution_district.district, own_costs = True)
