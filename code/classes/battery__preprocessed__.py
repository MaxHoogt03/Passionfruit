# NOTE: This file was automatically generated from:
# /mnt/c/Users/Max/Downloads/Passionfruit/code/classes/battery.py
# DO NOT CHANGE DIRECTLY! 1706728084.2877662
class Battery:

    def __init__(self, x, y, capacity):
        self.x = int(x)
        self.y = int(y)
        self.capacity = float(capacity)
        self.houses = []

    def get_location(self):
        """
        retrieves the x and y coordinate as a string.

        pre: none
        post: string

        """
        return f'{self.x},{self.y}'

    def change_location(self, x, y):
        """
        changes the location of the batteries.
        """
        self.x = x
        self.y = y

    def get_capacity(self):
        """
        retrieves the max capacity of the battery.

        pre: none
        post: string

        """
        return self.capacity

    def retract_capacity(self, house):
        """
        retracts capacity from battery by the output from a certain house.

        pre: output
        post: none
        """
        self.capacity -= house.get_output()

    def add_capacity(self, house):
        """
        retracts capacity from battery by the output from a certain house.

        pre: output
        post: none
        """
        self.capacity += house.get_output()

    def add_house(self, house):
        """
        Adds the house to a list.

        pre: House
        post: none

        side-effects: appends to self.houses.
        """
        self.houses.append(house)
        self.retract_capacity(house)

    def remove_house(self, house):
        """
        Removes the house from list.

        pre: House
        post: none

        side-effects: removes house from self.houses.
        """
        if house in self.houses:
            self.add_capacity(house)
            self.houses.remove(house)
        else:
            print(f'House {house} not found in the list of houses for Battery {self}')

    def get_houses(self):
        """
        returns the list of houses.

        pre: none
        post: list

        """
        return self.houses

    def __str__(self) -> str:
        """
        String representation of the battery.

        pre: none
        post: string

        """
        return f'Battery at coordinate {self.x}, {self.y} with capacity {self.capacity}'