import random


class Trainer:
    def __init__(self):
        pass

    def return_stats(self):
        pass

    def return_pokemon(self):
        pass

class Player(Trainer):
    def __init__(self, Name, PokeBalls:int = 3, PokeDollars:int = 500, Level:int = 2):
        self.Name = Name
        self.PokeBalls = PokeBalls
        self.PokeDollars = PokeDollars
        self.Level = Levels


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

        self.Pokemon = generatePokemon()
    
    def generatePokemon(self):
        pass

    def __repr__(self):
        return {
            "ID": self.ID,
            "Name": self.Name,
            "Level": self.Level
        }

demo = GenTrainer(3)
print(demo.__repr__())