import random
import pokemon as pk


class Trainer:
    def __init__(self):
        pass

    def return_stats(self):
        pass

    def return_pokemon(self):
        pass

class Player(Trainer):
    def __init__(self, Name, starter_pokemon,PokeBalls:int = 3, PokeDollars:int = 500, Level:int = 2):
        self.Name = Name
        self.PokeBalls = PokeBalls
        self.PokeDollars = PokeDollars
        self.Level = Level
        self.Pokemon = [pk.Pokemon(starter_pokemon)]

    


class GenTrainer(Trainer):
    ID = 0
    names = ["keith", "sam", "george"]
    def __init__(self, Level:int = 1):
        ID = GenTrainer.ID 
        names = GenTrainer.names

        ID += 1

        self.ID = ID
        self.Name = names[random.randint(0, (len(names) -1))]
        self.Level = Level

        self.Pokemon = self.generatePokemon()
    
    def generatePokemon(self):
        pokemon = []
        for x in range(self.Level):

            pokemon.append(pk.Pokemon())
        
        return pokemon

    def __str__(self):
        pokemon_list = "\n".join(
            f"  - {pokemon}" for pokemon in self.Pokemon
        )

        return (
            f"Trainer: {self.Name} (ID: {self.ID})\n"
            f"Level: {self.Level}\n"
            f"Pokémon ({len(self.Pokemon)}):\n"
            f"{pokemon_list}"
        )

    def __repr__(self):
        return (
            f"GenTrainer(ID={self.ID}, "
            f"Name={self.Name!r}, "
            f"Level={self.Level}, "
            f"Pokemon={self.Pokemon!r})"
        )

demo = GenTrainer(3)
print(demo.__repr__())