class House:
    def __init__(self, x, y, maxoutput) -> None:
        self.x = int(x)
        self.y = int(y)
        self.maxoutput = maxoutput
        self.cables = []
        self.score = 0

    
    def get_location(self):
        """
        retrieve x and y coordinate as a string.
        
        pre: none
        post: string

        """

        return f"{self.x},{self.y}"
    

    def get_output(self):
        """
        retrieves max output of the house
        
        pre: none
        post: float

        """

        return float(self.maxoutput)
    

    def add_cable(self, coordinates):
        """
        Add cable, by entering the end point of the cable.
        
        pre: string
        post: none

        side-effects: adds a list item to self.cables
        """

        self.cables.append(coordinates)

    def delete_cables(self):
        """
        Deletes all cables

        pre: none
        post: none

        side-effects: removes all items from self.cables
        """
        self.cables.clear()

    def get_cables(self):
        """
        Returns coordinates of cables.

        pre: none
        post: list
        
        """

        return self.cables
    

    def count_cables(self):
        """"
        Counts the amount of cables.

        pre: None
        post: int

        """

        return len(self.cables) - 1
    

    def __str__(self) -> str:
        """
        String representation of the house.

        pre: none
        post: string

        """
        
        return f"House at coordinate {self.x}, {self.y} with maxoutput {self.maxoutput}"