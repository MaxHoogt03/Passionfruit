"""
Relocates batteries with several options ranging from random to more sophisticated approaches.


"""

import csv
import random
from ..classes.house import House
from ..classes.battery import Battery
from ..classes.district import District
import copy

class Relocation:

    def __init__(self, district):
        self.district = district

    
    def randomise(self):
        """
        Changes the batteries to a random location.
        """
        index = 0
        houses = self.district.get_houses()
        for battery in self.district.get_batteries():
            battery.change_location(random.randint(0,50),random.randint(0,50))
            while index < len(self.district.get_houses()):
                if houses[index] == battery.get_location():
                    battery.change_location(random.randint(0,50),random.randint(0,50))
                    index = 0
                else:
                    index +=1
        return self.district
        

    
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
        
        copy_district = copy.deepcopy(self.district)
        best_houses = []
        list_of_houses = copy_district.get_houses()
        i = 0
        z = 0
        while i < 5:
            max_score_index = list_of_scores.index(max(list_of_scores))
            best_house = list_of_houses[max_score_index]
            for house in best_houses:
                if abs(best_house.x - house.x) <= optional_radius and abs(best_house.y - house.y) <= optional_radius:
                    list_of_houses.remove(best_house)
                    z = 1
                    break
            if z == 1:
                z = 0
                continue
            else: 
                best_houses.append(best_house)
                i +=1
        
        i = 0
        z = 0
        list_of_batteries = self.district.get_batteries()
        while i < 5:
            loc_house_x = best_houses[i].x
            loc_house_y = best_houses[i].y
            list_of_batteries[i].x = best_houses[i].x + random.randint(-1,1)
            list_of_batteries[i].y = best_houses[i].y + random.randint(-1,1)
            for house in self.district.get_houses():
                if house.get_location() == list_of_batteries[i].get_location():
                    z = 1
                    break
            if z == 1:
                z = 0
                continue
            else: 
                i += 1
                
               
            

            """Notes: je probeert hier de indexen op te slaan op de beste huizen, maar de beste huizen worden pas geselecteerd als ze meer dan de radius van
            elkaar afzitten, dus max huizen mogen niet dichterbij dan de radius bij elkaar zitten."""
        






