import random
import pokemon_data as pd

Pokemon_data = pd.Pokemon_data

class Pokemon:
    def __init__(self, species = None, level = 1):

        if species == None :
            species = random.choice(list(Pokemon_data.keys()))

        self.species = species
        self.name = species
        self.level = level

        species_info = Pokemon_data[self.species]

        self.element = species_info["element"]
        self.stats = species_info["base_stats"]
        self.moves = species_info["moves"]

    
    def __repr__(self):
        return f"Pokemon: {self.species} (Moves: {self.moves}, element(s): {self.element}, level: {self.level}, stats: {self.stats})"