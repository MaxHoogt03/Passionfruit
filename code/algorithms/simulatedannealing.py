import random
import math

from .hillclimber import Hillclimber

class SimulatedAnnealing(Hillclimber):

    def __init__(self, district, temperature = 1000):
        super().__init__(district)

        self.T0 = temperature
        self.T = temperature

    def update_temperature(self):

        # self.T = self.T - (self.T0 / self.iterations)
        cooling_factor = 0.95  # You can adjust this value
        self.T = self.T * cooling_factor

    def check_solution(self, new_district):
        new_costs = new_district.calculate_own_costs()
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
