class Battery:
    def __init__(self, x, y, capacity):
        self.x = x
        self.y = y
        self.capacity = capacity

    def __str__(self) -> str:
        return f"Battery at coordinate {self.x}, {self.y} with capacity {self.capacity}"
    
class House:
    def __init__(self, x, y, maxoutput) -> None:
        self.x = x
        self.y = y
        self.maxoutput = maxoutput

    def __str__(self) -> str:
        return f"House at coordinate {self.x}, {self.y} with maxoutput {self.maxoutput}"