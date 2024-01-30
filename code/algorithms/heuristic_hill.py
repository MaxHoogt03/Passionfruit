import copy

from ..classes.district import District
from ..classes.queue import Queue

class Heuristic_Hill:
    """
    A class to perform iterative optimization for connecting houses to batteries in a district.
    """
    def __init__(self, district, own_costs = True):
        """
        Initialize the Iterative optimizer.

        pre:
            - district
            - own_costs: A boolean flag indicating whether to use own costs (True) or shared costs (False) for calculations.

        post:
            - A deep copy of the district
            - A queue to track the last 130 processed houses
            - The costs based on the 'own_costs' boolean
        """
        self.district = copy.deepcopy(district)
        self.own_costs = own_costs

    def furthest_house(self):
        """
        Identify the house and its connected battery that are furthest apart in the district.

        post:
            - The furthest house from its battery ('dumb_house') and its connected battery ('dumb_battery')
            - The identified house is enqueued into 'last_130_houses'
        """
        longest_distance = 0
        self.dumb_battery = None
        self.dumb_house = None
        for battery in self.district.get_batteries():
            for house in battery.get_houses():
                new_distance = District.calculate_distance(house, battery)
                if new_distance > longest_distance and house not in self.last_130_houses.items:
                    longest_distance = new_distance
                    self.dumb_house = house
                    self.dumb_battery = battery
        self.last_130_houses.enqueue(self.dumb_house)
        if self.last_130_houses.size() > 130:
            self.last_130_houses.dequeue()
        # Retrieve the batteries in list sorted on distance to dumb_house
        self.sorted_batteries = sorted(self.district.get_batteries(), key=lambda battery: District.calculate_distance(self.dumb_house, battery))

    def replace_battery(self):
        """
        Attempt to find a closer battery for the identified house and swap connections if it reduces costs and meets capacity constraints.

        post:
            - If a suitable replacement battery is found, houses are swapped between the old and new batteries
        """
        for i in range(len(self.sorted_batteries)):
            self.new_battery = self.sorted_batteries[i]
            if self.new_battery is not None:
                #print('found new battery')
                for self.new_house in self.new_battery.get_houses():
                    if self.conditions():
                        self.swap_houses()
                        break

    def conditions(self):
        """
        Check if swapping the houses between batteries reduces the total cable length and respects battery capacities.

        post:
            - Returns True if swapping is beneficial and feasible, False otherwise.
        """
        if District.calculate_distance(self.new_house, self.new_battery) + District.calculate_distance(self.dumb_house, self.dumb_battery) > District.calculate_distance(self.new_house, self.dumb_battery) + District.calculate_distance(self.dumb_house, self.new_battery) and \
        self.new_battery.get_capacity() + self.new_house.get_output() - self.dumb_house.get_output() > 0 and self.dumb_battery.get_capacity() + self.dumb_house.get_output() - self.new_house.get_output() > 0:
            return True
        return False

    def swap_houses(self):
        """
        Perform the actual swap of houses between the two batteries.

        post:
            - The houses are swapped between the two batteries, and new cable connections are made.
        """
        self.new_house.delete_cables()
        self.add_greedy_connection(self.new_house, self.dumb_battery)
        self.dumb_house.delete_cables()
        self.add_greedy_connection(self.dumb_house, self.new_battery)
        self.new_battery.remove_house(self.new_house)
        self.new_battery.add_house(self.dumb_house)
        self.dumb_battery.remove_house(self.dumb_house)
        self.dumb_battery.add_house(self.new_house)
        self.dumb_battery = self.new_battery

    def add_greedy_connection(self, house, battery):
        """
        Adds the cables by first clearing the x difference between the house and battery and then y.

        pre:
            - house object
            - battery object

        post:
            - Cables are added between the house and the battery.
        """
        dist_x = house.x - battery.x
        dist_y = house.y - battery.y

        # Adds the cables to the houses, by first walking over the x difference and then the y difference.
        if dist_x <= 0:
            for i in range(abs(dist_x)):
                house.add_cable(f"{house.x + i}, {house.y}")

        elif dist_x >= 0:
            for i in range(dist_x):
                house.add_cable(f"{house.x - i}, {house.y}")

        if dist_y <= 0:
            for i in range(abs(dist_y) + 1):
                house.add_cable(f"{house.x - dist_x}, {house.y + i}")

        elif dist_y >= 0:
            for i in range(dist_y + 1):
                house.add_cable(f"{house.x - dist_x}, {house.y - i}")

    def run(self):
        self.last_130_houses = Queue()
        for i in range(150):
            self.furthest_house()
            self.replace_battery()
        if self.own_costs:
            self.costs = self.district.calculate_own_costs()
        else:
            self.costs = self.district.calculate_shared_costs()

        return self.district