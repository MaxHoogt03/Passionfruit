import random
import math

from .hillclimber import Hillclimber

class SimulatedAnnealing(Hillclimber):

    def __init__(self, district, temperature = 1000, own_costs = True):
        super().__init__(district, own_costs)

        self.T0 = temperature
        self.T = temperature

    def update_temperature(self):

        # self.T = self.T - (self.T0 / self.iterations)
        cooling_factor = 0.997  # You can adjust this value
        self.T = self.T * cooling_factor

    def check_solution(self, new_district):
        if self.own_costs:
            new_costs = new_district.calculate_own_costs()
        else:
            new_costs = new_district.calculate_shared_costs()
        old_costs = self.costs

        delta = new_costs - old_costs
        try:
            probability = math.exp(-delta / self.T)
        except OverflowError:
            probability = float('inf')

        r = random.random()

        if r < probability:
            self.district = new_district
            self.costs = new_costs

        self.update_temperature()
