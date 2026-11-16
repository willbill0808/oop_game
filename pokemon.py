import random
import pokemon_data as pd

Pokemon_data = pd.Pokemon_data

class Pokemon:
    def __init__(self, species, level = 1):
        self.species = species
        self.name = species
        self.level = level

        species_info = Pokemon_data[self.species]

        self.element = species_info["element"]
        self.stats = species_info["base_stats"]

    
    def __repr__(self):
        return f"Pokemon: {self.species} (Name: {self.name}, element(s): {self.element}, level: {self.level}, stats: {self.stats})"


p1 = Pokemon("squirtle")

print(p1)