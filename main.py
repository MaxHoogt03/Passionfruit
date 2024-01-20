from code.classes import battery, district, house
import matplotlib.pyplot as plt
from code.algorithms import more_random as mr, random_to_greedy as rtg, greedy as gr, hillclimber as hc

if __name__ == "__main__":
    district_1 = district.District(1, "data/district_1/district-1_")
    district_2 = district.District(2, "data/district_2/district-2_")
    district_3 = district.District(3, "data/district_3/district-3_")


    # --------------------------- Heatmap -------------------------
    district_1.heatmap()
    district_2.heatmap()
    district_3.heatmap()

    # --------------------------- Random --------------------------
    # random_solution_district_1 = mr.random_solution(district_1)
    # print(random_solution_district_1.district.calculate_own_costs())
    
    # # Histogram to see how the random cable length is distributed
    # results = []
    # for i in range(0):
    #     result = more_random.random_solution(district_1)
    #     results.append(result)
    # plt.hist(results, bins=20)
    # plt.title('Histogram of Results')
    # plt.xlabel('Result Value')
    # plt.ylabel('Frequency')
    # plt.savefig('plot.png')

    # --------------------------- Random to Greedy --------------------------
    random_solution_district_1 = rtg.RandomGreedy(district_1)
    random_solution_district_1.greedy_solution()
    random_solution_district_1.district.plot_cables()
    # random_solution_district_1.district.output()
    # --------------------------- Greedy --------------------------
    # print(greedy.greedy_solution(district_3))

    # --------------------------- Random to Hillclimber -----------------------------
    hillclimber_1 = hc.Hillclimber(random_solution_district_1.district)
    hillclimber_1.run(10000, True)