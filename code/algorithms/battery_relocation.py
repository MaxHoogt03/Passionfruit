"""
Relocates batteries with several options ranging from random to more sophisticated approaches.


"""

import csv
import random
from ..classes.house import House
from ..classes.battery import Battery
from ..classes.district import District

class Relocation:

    def __init__(self, district):
        self.district = district

    
    def randomise(self):
        """
        Changes the batteries to a random location.
        """
        for battery in self.district.get_batteries():
            battery.change_location(random.randint(0,50),random.randint(0,50))

    
    def most_houses(self, optional_radius = 5):
        
        list_of_houses = self.district.get_houses()
        list_of_scores = []
        for house in list_of_houses:
            score = 0
            location_target_x = house.x
            location_target_y = house.y

            for i in range(0, len(list_of_houses)):
                location_rest_x = list_of_houses[i].x 
                location_rest_y = list_of_houses[i].y
                
                if abs(location_target_x - location_rest_x) <= optional_radius and abs(location_target_y - location_rest_y) <= optional_radius:
                    score +=1

            if score > 0:
                score = score - 1

            house.score = score
            list_of_scores.append(score)
        
        best_houses = []
        for i in range(0,5):
            max_score_index = 
            """Notes: je probeert hier de indexen op te slaan op de beste huizen, maar de beste huizen worden pas geselecteerd als ze meer dan de radius van
            elkaar afzitten, dus max huizen mogen niet dichterbij dan de radius bij elkaar zitten."""
        






