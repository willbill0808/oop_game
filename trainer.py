import random


class Trainer:
    def __init__(self):
        pass

    def return_stats(self):
        pass

    def return_pokemon(self):
        pass

class GenTrainer(Trainer):
    ID = 0
    names = ["keith", "sam", "george"]
    def __init__(self, Level = 1):
        GenTrainer.ID += 1
        names = GenTrainer.names

        self.ID = GenTrainer.ID
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