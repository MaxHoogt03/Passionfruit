import random
import copy

from .heuristic_hill import Heuristic_Hill

class Genetic:
    def __init__(self, initial_population, crossover_rate, mutation_rate, district):
        self.population = initial_population
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.district = district

    def crossover_genes_uniform(self, parent1, parent2):
        offspring = copy.deepcopy(self.district)

        # Sort houses by coordinates before crossover
        houses_parent1 = sorted(parent1.get_houses(), key=lambda house: (house.x, house.y))
        houses_parent2 = sorted(parent2.get_houses(), key=lambda house: (house.x, house.y))

        for house1, house2 in zip(houses_parent1, houses_parent2):
            # Randomly choose whether to inherit connections from parent1 or parent2
            if random.random() < 0.5:
                inherited_connections = house1.get_cables() 
                house = house1
                
            else:
                inherited_connections = house2.get_cables()
                house = house2

            # Copy the connections to the offspring's house
            offspring_house = offspring.find_corresponding_house(house)
            offspring_battery = offspring.find_corresponding_battery(inherited_connections[-1])
            offspring_battery.add_house(offspring_house)

            for cable in inherited_connections:
                offspring_house.add_cable(cable)

        return offspring


    def repair_capacity_constraint(self, offspring):
        offspring_copy = copy.deepcopy(offspring)
        iteration = 100

        while any(battery.get_capacity() < 0 for battery in offspring_copy.get_batteries()):
            negative_capacity = sum(min(0, battery.get_capacity()) for battery in offspring_copy.get_batteries())
            
            offspring_copy = self.mutate_to_repair(offspring_copy, negative_capacity, iteration)
            if offspring_copy == "Retry":
                return "Retry"
            else:
                continue

        offspring = offspring_copy

        return offspring
                    

    def mutate_to_repair(self, offspring, negative_capacity, iteration):
        offspring_copy = copy.deepcopy(offspring)

        if iteration <= 0:
            return "Retry"

        while iteration > 0:
            iteration -= 1
            battery_1, battery_2 = random.sample(offspring_copy.get_batteries(), 2)
            if battery_1.get_capacity() < 0 and battery_2.get_capacity() > 0 or battery_1.get_capacity() > 0 and battery_2.get_capacity() < 0:
                break

        house_1 = random.choice(battery_1.get_houses())
        house_2 = random.choice(battery_2.get_houses())

        house_1.delete_cables()
        house_2.delete_cables()

        battery_1.remove_house(house_1)
        battery_2.remove_house(house_2)

        self.add_connection(house_1, battery_2)
        self.add_connection(house_2, battery_1)

        battery_1.add_house(house_2)
        battery_2.add_house(house_1)

        new_negative_capacity = sum(min(0, battery.get_capacity()) for battery in offspring_copy.get_batteries())

        if new_negative_capacity > negative_capacity:
            return offspring_copy
        
        else:
            return self.mutate_to_repair(offspring, negative_capacity, iteration - 1)

    def add_connection(self, house, battery):
        """
        Adds the cables by first clearing the x difference between the house and battery and then y.
        """
        x_house = house.x
        y_house = house.y
        x_battery = battery.x
        y_battery = battery.y
        dist_x = x_house - x_battery
        dist_y = y_house - y_battery

        # Adds the cables to the houses, by first walking over the x difference and then the y difference.
        if dist_x <= 0:
            for i in range(abs(dist_x)):
                house.add_cable(f"{x_house + i}, {y_house}")

        elif dist_x >= 0:
            for i in range(dist_x):
                house.add_cable(f"{x_house - i}, {y_house}")

        if dist_y <= 0:
            for i in range(abs(dist_y) + 1):
                house.add_cable(f"{x_house - dist_x}, {y_house + i}")

        elif dist_y >= 0:
            for i in range(dist_y + 1):
                house.add_cable(f"{x_house - dist_x}, {y_house - i}")

    def mutate(self, solution):
        mutation = Heuristic_Hill(solution)
        return mutation.district

    def generate_next_generation(self):
        new_generation = []

        random.shuffle(self.population)

        for i in range(0, len(self.population) - 1, 2):
            parent1 = self.population[i]
            parent2 = self.population[i + 1]

            # print(f"Iteration: {int(i/2+1)}")

            # Apply crossover with a certain probability
            if random.random() < self.crossover_rate:
                child1 = self.crossover_genes_uniform(parent1, parent2)
                child1 = self.repair_capacity_constraint(child1)

                while child1 == "Retry":
                    child1 = self.crossover_genes_uniform(parent1, parent2)
                    child1 = self.repair_capacity_constraint(child1)

                # Apply mutation with a certain probability
                if random.random() < self.mutation_rate:
                    child = self.mutate(child)

                new_generation.append(child)

            else:
                new_generation.extend([parent1, parent2])

        new_generation.sort(key=self.evaluate_fitness)

        self.population = new_generation
        print(len(new_generation), new_generation[0].calculate_own_costs())
        return new_generation
    
    def run(self, generations):
        for i in range(generations):
            print(f"Generation: {i+1}")
            self.generate_next_generation()

        # Choose the best solution from the final population
        best_solution = min(self.population, key=self.evaluate_fitness)
        return best_solution

    def evaluate_fitness(self, solution):
        # Implement your fitness evaluation logic
        # This could involve calculating the total cost or other relevant metrics
        return solution.calculate_own_costs()
