import csv

class Battery:
    def __init__(self, x, y, capacity):
        self.x = int(x)
        self.y = int(y)
        self.capacity = capacity
        self.houses = []    
    
    def get_location(self):
        """
        retrieves the x and y coordinate as a string.

        pre: none
        post: string

        """
        return f"{self.x},{self.y}"
    
    
    def get_capacity(self):
        """
        retrieves the max capacity of the battery.

        pre: none
        post: string

        """
        return self.capacity
    

    def add_house(self, house):
        """
        Adds the house to a list.

        pre: House
        post: none

        side-effects: appends to self.houses.
        """
        self.houses.append(house)
    

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
        return f"Battery at coordinate {self.x}, {self.y} with capacity {self.capacity}"
    