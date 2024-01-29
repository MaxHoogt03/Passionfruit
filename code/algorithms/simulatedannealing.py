import random
import math

from .hillclimber import Hillclimber

class SimulatedAnnealing(Hillclimber):

    def __init__(self, district, temperature = 50, own_costs = True):
        super().__init__(district, own_costs)

        self.T0 = temperature
        self.T = temperature

    def update_temperature(self):
        if self.iterations < 2000:
            self.T = 0
        elif self.iterations < 5000:
            cooling_factor = 30 / 3000
            self.T = 30 - cooling_factor * (self.iterations - 2000)
        else:
            self.T = 0


    def check_solution(self, new_district):
        if self.own_costs:
            new_costs = new_district.calculate_own_costs()
        else:
            new_costs = new_district.calculate_shared_costs()
        old_costs = self.costs

        delta = new_costs - old_costs

        try:
            if self.T != 0:
                probability = math.exp(-delta / self.T)
            else:
                probability = 1 if delta < 0 else 0
        except OverflowError:
            probability = float('inf')

        r = random.random()

        if r < probability:
            self.district = new_district
            self.costs = new_costs

        self.update_temperature()
