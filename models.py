import csv

class Battery:
    def __init__(self, x, y, capacity):
        self.x = int(x)
        self.y = int(y)
        self.capacity = capacity

    def read_battery(filename):
        battery_list = []

        with open(f'data/district_1/{filename}', 'r') as file:
            csv_reader = csv.DictReader(file)

            for row in csv_reader:
                x, y = row['positie'].split(',')
                capacity = row['capaciteit']
                battery_list.append(Battery(x, y, capacity))

        return battery_list
    
    def __str__(self) -> str:
        return f"Battery at coordinate {self.x}, {self.y} with capacity {self.capacity}"
    
class House:
    def __init__(self, x, y, maxoutput) -> None:
        self.x = int(x)
        self.y = int(y)
        self.maxoutput = maxoutput

    def read_house(filename):
        house_list = []

        with open(f'data/district_1/{filename}', 'r') as file:
            csv_reader = csv.DictReader(file)

            for row in csv_reader:
                x = row['x']
                y = row['y']
                maxoutput = row['maxoutput']
                house_list.append(House(x, y, maxoutput))

        return house_list

    def __str__(self) -> str:
        return f"House at coordinate {self.x}, {self.y} with maxoutput {self.maxoutput}"