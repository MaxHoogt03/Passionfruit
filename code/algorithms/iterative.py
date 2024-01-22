import copy

from ..classes.district import District
from ..classes.queue import Queue

class Iterative:
    def __init__(self, district):
        self.district = copy.deepcopy(district)
        self.last_130_houses = Queue()
        for i in range(150):
            self.furthest_house()
            self.replace_battery()
        self.run()

    def furthest_house(self):
        # Retrieve house and battery furthest seperated
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
        # if a battery closer is found, check whether it saves costs and the capacities are appropriate
        for i in range(len(self.sorted_batteries)):
            self.new_battery = self.sorted_batteries[i]
            if self.new_battery is not None:
                #print('found new battery')
                for self.new_house in self.new_battery.get_houses():
                    if self.conditions():
                        self.swap_houses()
                        break

    def conditions(self):
        if District.calculate_distance(self.new_house, self.new_battery) + District.calculate_distance(self.dumb_house, self.dumb_battery) > District.calculate_distance(self.new_house, self.dumb_battery) + District.calculate_distance(self.dumb_house, self.new_battery) and \
        self.new_battery.get_capacity() + self.new_house.get_output() - self.dumb_house.get_output() > 0 and self.dumb_battery.get_capacity() + self.dumb_house.get_output() - self.new_house.get_output() > 0:
            return True
        return False

    def swap_houses(self):
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
        """
        dist_x = house.x - battery.x
        dist_y = house.y - battery.y

        # Adds the cables to the houses, by first walking over the x difference and then the y difference.
        if dist_x < 0:
            for i in range(abs(dist_x)):
                house.add_cable(f"{house.x + i}, {house.y}")

        elif dist_x > 0:
            for i in range(dist_x):
                house.add_cable(f"{house.x - i}, {house.y}")

        if dist_y < 0:
            for i in range(abs(dist_y) + 1):
                house.add_cable(f"{house.x - dist_x}, {house.y + i}")

        elif dist_y > 0:
            for i in range(dist_y + 1):
                house.add_cable(f"{house.x - dist_x}, {house.y - i}")

    def run(self):
        
        print(self.district.calculate_own_costs())
        return self.district