import random
import copy

from ..classes.district import District

def randomize_houses(district):
    """
    Creates a deep copy of the list of houses and randomly shuffles this list.
    """
    random.shuffle(district.get_houses())

def greedy_solution(district):
    retry = True
    while retry:
        district_copy = copy.deepcopy(district)
        randomize_houses(district_copy)

        total_min_distance = 0
        retry = False  # Reset the retry flag at the beginning of each attempt
        for house in district_copy.houses:
            smallest_distance = None
            closest_battery = None

            # loops over all batteries and checks which battery is closest to current house, with its distance.
            for battery in district_copy.batteries:
                distance = District.calculate_distance(house, battery)
                
                if (smallest_distance is None or distance < smallest_distance) and battery.get_capacity() >= house.get_output():
                    smallest_distance = distance
                    closest_battery = battery
            
            if closest_battery is not None:
                # Variables for location of current house, closest battery, and the distance.
                x_house = house.x
                y_house = house.y
                x_battery = closest_battery.x
                y_battery = closest_battery.y
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
                total_min_distance += smallest_distance

                # Retract the output from the house from the capacity of the battery.
                closest_battery.retract_capacity(house.get_output())

                # Adds to house to the current battery object.
                closest_battery.add_house(house)
            else:
                # If no suitable battery is found for a house, set the retry flag and break the loop
                print("Retrying")
                retry = True
                break

    district_copy.output()
    print(district_copy.calculate_own_costs())
    district_copy.plot_cables()
