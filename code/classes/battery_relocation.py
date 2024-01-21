"""
Relocates batteries with several options ranging from random to more sophisticated approaches.


"""

import csv
import random

class Relocation:

    def __init__(self, file_path):
        self.csv_url = file_path

    def Randomise(self):
        
        # reads the districts batteriesfile
        with open(f"{self.file_path}batteries.csv","r") as file:
            csv_reader = csv.DictReader(file)
            next(csv_reader)

            capacity_list = []
            for row in csv_reader:
                capacity_list.append(row["capaciteit"])

        # storage for the data that needs to be written to the csv file.
        data = []
        # make the data
        for i in range(0,5):
            x_position = random.randint(0,50)
            y_position = random.randint(0,50)
            data.append({
                "positie": f"{x_position}, {y_position}",
                "capaciteit": capacity_list[i]
                })
        
        # writes the positions to a randomised file.
        with open(f"{self.file_path}Randomised_batteries.csv", "w", newline = '') as csvfile:
            fieldnames = ['positie', 'capaciteit']

            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for row in data:
                writer.writerow(row)




