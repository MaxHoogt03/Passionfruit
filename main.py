from code.classes import battery, district, house

from code.algorithms import randomise

if __name__ == "__main__":
    district_1 = district.District(1, "data/district_1/district-1_")
    sum = 0
    for item in district_1.houses:
        sum += item.get_output()

    print(sum)
    randomise.random_solution(district_1)