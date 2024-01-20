import copy
import random

from ..classes.district import District

class Hillclimber:
    MAX_ITERATIONS = 100

    def __init__(self, district):
        self.district = copy.deepcopy(district)
        self.costs = district.calculate_own_costs()

    def add_connection(self, house, battery):
        """
        Adds the cables by first clearing the x difference between the house and battery and then y.
        """
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
                house.add_cable(f"{x_house - i}, {y_house}")

        if dist_y < 0:
            for i in range(abs(dist_y) + 1):
                house.add_cable(f"{x_house - dist_x}, {y_house + i}")

        elif dist_y > 0:
            for i in range(dist_y + 1):
                house.add_cable(f"{x_house - dist_x}, {y_house - i}")

    def mutate_random_connection(self, district, iterations = MAX_ITERATIONS):
        battery_1, battery_2 = random.sample(district.get_batteries(), 2)
        house_1 = random.choice(battery_1.get_houses())
        house_2 = random.choice(battery_2.get_houses())

        if battery_1.get_capacity() + house_1.get_output() < house_2.get_output() or battery_2.get_capacity() + house_2.get_output() < house_1.get_output() and iterations > 0:
            self.mutate_random_connection(district, iterations-1)

        elif iterations <= 0:
            print("Could not find better random connection.")

        else:
            house_1.delete_cables()
            house_2.delete_cables()

            battery_1.add_capacity(house_1.get_output())
            battery_2.add_capacity(house_2.get_output())

            battery_1.remove_house(house_1)
            battery_2.remove_house(house_2)

            self.add_connection(house_1, battery_2)
            self.add_connection(house_2, battery_1)

            battery_1.add_house(house_2)
            battery_2.add_house(house_1)

            battery_1.retract_capacity(house_2.get_output())
            battery_2.retract_capacity(house_1.get_output())

    def check_solution(self, new_district):
        new_costs = new_district.calculate_own_costs()
        old_costs = self.costs


        if new_costs <= old_costs:
            self.district = new_district
            self.costs = new_costs

    def run(self, iterations, verbose=False):

        for i in range(iterations):
            print(f"Iteration {i}/{iterations}, current value: {self.costs}") if verbose else None

            new_district = copy.deepcopy(self.district)
            self.mutate_random_connection(new_district)

            self.check_solution(new_district)