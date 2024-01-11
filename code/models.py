class Battery:
    def __init__(self, x, y, capacity):
        self.x = int(x)
        self.y = int(y)
        self.capacity = capacity

    def __str__(self) -> str:
        return f"Battery at coordinate {self.x}, {self.y} with capacity {self.capacity}"
    
class House:
    def __init__(self, x, y, maxoutput) -> None:
        self.x = int(x)
        self.y = int(y)
        self.maxoutput = maxoutput
        self.cables = []


    def __str__(self) -> str:
        return f"House at coordinate {self.x}, {self.y} with maxoutput {self.maxoutput}"
    

    def add_cable(self, coordinates):
        """
        Add cable, by entering the end point of the cable.
        
        pre: list[int,int]
        post: none

        side-effects: adds a list item to self.cables
        """
        self.cables.append(coordinates)
    
