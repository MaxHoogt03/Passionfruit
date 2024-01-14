from code.classes import battery, district, house

from code.algorithms import randomise

if __name__ == "__main__":
    district_2 = district.District(2, "data/district_2/district-2_")
    randomise.random_solution(district_2)