
pokemon = [
    [1, "water-type", {
        "speed": 3,
        "attack": 2,
        "defense": 1
    }],
    [2, "fire-type", {
        "speed": 1,
        "attack": 3,
        "defense": 2
    }],
    [3, "nature-type", {
        "speed": 2,
        "attack": 1,
        "defense": 3
    }]
]

player_name = input("What is your name\n: ")
print(f"Your name is {player_name}! \nYour options for starter pokemon are:")
for mon in pokemon:
    pokeID = mon[0]
    pokeName = mon[1]
    print(f"Option {pokeID} is {pokeName}")
starter_pokemon = input(f"What is your choice, pick using the numbers 1-{len(pokemon)}\n(1-{len(pokemon)}): ")


"""
game_running = True

while game_running:
    print(pokemon)
    game_running = False

"""
