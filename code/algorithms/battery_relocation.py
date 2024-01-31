"""
Relocates batteries with several options ranging from random a more sophisticated approach.


"""

import csv
import random
from ..classes.house import House
from ..classes.battery import Battery
from ..classes.district import District
import copy

class Relocation:

    def __init__(self, district):
        """
        Initializing the Relocation class.
        """
        self.district = district

    
    def randomise(self):
        """
        Changes the batteries to a random location.
        """
        index = 0

        # Store the list of houses in the district to make sure no batteries are placed on houses.
        houses = self.district.get_houses()
        for battery in self.district.get_batteries():

            # Changing the location to a random place on the grid.
            battery.change_location(random.randint(0,50),random.randint(0,50))
            while index < len(self.district.get_houses()):

                # If it lands on a house, we relocate the battery and restart the loop.
                if houses[index] == battery.get_location():
                    battery.change_location(random.randint(0,50),random.randint(0,50))
                    index = 0
                else:
                    index +=1

        return self.district
        

    
    def most_houses(self, optional_radius = 5):
        """
        Changes the location of the batteries with the folowing algoritm: 

        1. give the houses points based on how many houses are within the optional_radius
        2. Place the first battery near the house with the most points.
        3. For the folowing batteries the code places the batteries outside the optional_radius of the chosen houses to prevent 
        clutching of batteries.

        """

       # Get a list of houses from the district
        list_of_houses = self.district.get_houses()
        list_of_scores = []

        # Calculate scores for each house based on the number of other houses within optional_radius
        for house in list_of_houses:
            score = 0
            location_target_x = house.x
            location_target_y = house.y

            # Check proximity of each house to the target house
            for i in range(0, len(list_of_houses)):
                location_rest_x = list_of_houses[i].x 
                location_rest_y = list_of_houses[i].y
                
                # add score if the house is within the specified radius
                if abs(location_target_x - location_rest_x) <= optional_radius and abs(location_target_y - location_rest_y) <= optional_radius:
                    score += 1

            # Adjust the score to avoid counting the target house itself
            if score > 0:
                score = score - 1

            # Assign the calculated score to the house and add it to the list
            house.score = score
            list_of_scores.append(score)

        # Create a deep copy of the district to avoid modifying the original district
        copy_district = copy.deepcopy(self.district)
        best_houses = []

        
        list_of_houses = copy_district.get_houses()
        i = 0
        z = 0

        # Select the top 5 houses with the highest scores
        while i < 5:

            # Find the index of the house with the highest score
            max_score_index = list_of_scores.index(max(list_of_scores))
            best_house = list_of_houses[max_score_index]

            # Check if the selected house is too close to previously selected best houses
            for house in best_houses:
                if abs(best_house.x - house.x) <= optional_radius and abs(best_house.y - house.y) <= optional_radius:

                    # If too close, remove the house from consideration
                    list_of_houses.remove(best_house)
                    z = 1
                    break

            if z == 1:
                # Reset flag and continue to the next iteration
                z = 0
                continue

            else: 
                # Add the selected best house to the list
                best_houses.append(best_house)
                i += 1

        
        i = 0
        z = 0
        list_of_batteries = self.district.get_batteries()

        # Move each battery to a random location near its corresponding best house
        while i < 5:
            loc_house_x = best_houses[i].x
            loc_house_y = best_houses[i].y

            # Place the battery randomly near the next best house
            list_of_batteries[i].x = best_houses[i].x + random.randint(-1, 1)
            list_of_batteries[i].y = best_houses[i].y + random.randint(-1, 1)

            # Check if the new battery location overlaps with existing houses
            for house in self.district.get_houses():
                if house.get_location() == list_of_batteries[i].get_location():
                    z = 1
                    break

            if z == 1:
                # If overlap, reset flag and continue to the next iteration
                z = 0
                continue

            else: 
                # Move to the next battery
                i += 1







