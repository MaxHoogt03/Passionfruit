import csv

class Battery:
    def __init__(self, x, y, capacity):
        self.x = int(x)
        self.y = int(y)
        self.capacity = capacity
        self.houses = []

    def read_battery(filename):
        battery_list = []

        with open(f'{filename}', 'r') as file:
            csv_reader = csv.DictReader(file)

            for row in csv_reader:
                x, y = row['positie'].split(',')
                capacity = row['capaciteit']
                battery_list.append(Battery(x, y, capacity))

        return battery_list
    
    def get_location(self):
        return f"{self.x},{self.y}"
    
    def get_capacity(self):
        return self.capacity
    
    def add_house(self, house):
        self.houses.append(house)
    
    def get_houses(self):
        return self.houses
    
    def __str__(self) -> str:
        return f"Battery at coordinate {self.x}, {self.y} with capacity {self.capacity}"
    