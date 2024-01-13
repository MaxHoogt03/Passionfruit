from code.classes import battery, district, house

from code.algorithms import randomise

if __name__ == "__main__":
    district_1 = district.District(1, "data/district_1/district-1_")
    randomise.random_solution(district_1)