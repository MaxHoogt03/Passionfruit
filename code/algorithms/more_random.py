import random
import copy

from ..classes.district import District

def randomize_houses(district):
    """
    Creates a deep copy of the list of houses and randomly shuffles this list.
    """
    random.shuffle(district.get_houses())

def random_solution(district):
    retry = True
    while retry:
        district_copy = copy.deepcopy(district)
        randomize_houses(district_copy)

        total_min_distance = 0
        retry = False  # Reset the retry flag at the beginning of each attempt
        for house in district_copy.houses:
            distance = None
            battery = None
            random.shuffle(district_copy.batteries)
            # loops over all batteries and checks which battery is closest to current house, with its distance.
            for battery in district_copy.batteries:
                if battery.get_capacity() >= house.get_output():
                    distance = District.calculate_distance(house, battery)
                    break
            
            if battery is not None and distance is not None:
                # Variables for location of current house, closest battery, and the distance.
                x_house = house.x
                y_house = house.y
                x_battery = battery.x
                y_battery = battery.y
                dist_x = x_house - x_battery
                dist_y = y_house - y_battery

                # Adds the cables to the houses, by first walking over the x difference and then the y difference.
                if dist_x < 0:
                    for i in range(abs(dist_x)):
                        house.add_cable(f"{x_house + i}, {y_house}")
                
                elif dist_x > 0:
                    for i in range(dist_x):
                        house.add_cable(f"{x_house-i}, {y_house}")

                if dist_y < 0:
                    for i in range(abs(dist_y) + 1):
                        house.add_cable(f"{x_house - dist_x}, {y_house + i}")
                
                elif dist_y > 0:
                    for i in range(dist_y + 1):
                        house.add_cable(f"{x_house-dist_x}, {y_house - i}")

                # Adds all distances of the houses to their closest battery.
                total_min_distance += distance

                # Retract the output from the house from the capacity of the battery.
                battery.retract_capacity(house.get_output())

                # Adds to house to the current battery object.
                battery.add_house(house)
            else:
                # If no suitable battery is found for a house, set the retry flag and break the loop
                print("Retry")
                retry = True
                break

    district_copy.output()
    return district_copy.calculate_own_costs()
