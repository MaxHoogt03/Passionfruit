import csv

class House:
    def __init__(self, x, y, maxoutput) -> None:
        self.x = int(x)
        self.y = int(y)
        self.maxoutput = maxoutput
        self.cables = []

    def read_house(filename):
        house_list = []

        with open(f'{filename}', 'r') as file:
            csv_reader = csv.DictReader(file)

            for row in csv_reader:
                x = row['x']
                y = row['y']
                maxoutput = row['maxoutput']
                house_list.append(House(x, y, maxoutput))

        return house_list

    def __str__(self) -> str:
        return f"House at coordinate {self.x}, {self.y} with maxoutput {self.maxoutput}"
    
    def add_cable(self, coordinates):
        """
        Add cable, by entering the end point of the cable.
        
        pre: string
        post: none

        side-effects: adds a list item to self.cables
        """
        self.cables.append(coordinates)

    def get_cables(self):
        """
        Returns coordinates of cables.
        
        """
        return self.cables