from code.classes import battery, district, house
import matplotlib.pyplot as plt
from code.algorithms import more_random, random_to_greedy, greedy

if __name__ == "__main__":
    district_1 = district.District(1, "data/district_1/district-1_")
    district_2 = district.District(2, "data/district_2/district-2_")
    district_3 = district.District(3, "data/district_3/district-3_")


    # --------------------------- Heatmap -------------------------
    district_1.heatmap()
    district_2.heatmap()
    district_3.heatmap()

    # --------------------------- Random --------------------------
    print(more_random.random_solution(district_1))
    
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
    # random_to_greedy.greedy_solution(district_1)

    # --------------------------- Greedy --------------------------
    # print(greedy.greedy_solution(district_3))