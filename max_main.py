from code.classes import district

from code.algorithms import advanced_6 as a6

district_1 = district.District(1, "data/district_1/district-1_")

instance = a6.Advanced_6(district_1)
print(instance.random_battery_list(7500))