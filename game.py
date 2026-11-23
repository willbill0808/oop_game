import random
import pokemon_data as pd
import trainer 

Player = trainer.Player # the Player class
GenTrainer = trainer.GenTrainer # the generic Trainer class


def genFight(player):
    enemy = GenTrainer()
    enemyMon = enemy.Pokemon[0]
    playerMon = player.Pokemon[0]

    print(f"Your opponent :{enemyMon}")
    print(f"your battler : {playerMon}")

    if playerMon.stats["speed"] >= playerMon.stats["speed"]: # Decides the pokemon to go first each turn
        faster = playerMon
        slower = enemyMon
    else :
        faster = enemyMon
        slower = playerMon

    while enemyMon.stats["hp"] >= 0 and playerMon.stats["hp"] >= 0: # While both pokemon are alive
        print(f"\n{faster.name} used the move {faster.moves[0]}")
        damage = random.randint(5,15)
        slower.stats["hp"] = slower.stats["hp"] - damage
        print(f"it did {damage} points of damage")

        if slower.stats["hp"] <= 0: # Sees if the slower pokemon is still alive after the attack
            break 

        damage = random.randint(5,15)
        print(f"\n{slower.name} used the move {slower.moves[0]}")
        faster.stats["hp"] = faster.stats["hp"] - damage
        print(f"it did {damage} points of damage")

        print(f"\n {playerMon.name} has {playerMon.stats["hp"]} hp")
    
    if playerMon.stats["hp"] <= 0: # Tells you the loser after the battle (after the break from the while-loop)
        print("you lost")
    else: 
        print("you won")


def main(player):
    run = True
    while run: # runs the game loop while run is true
        choice = int(input("\nWhat do you want to do now? \n1. Hunt for pokemon \n2. Go to the shop \n3. Fight other trainers for money \n4. Fight the gym leader\n(1-4(3 er den eneste som er ferdig)): "))

        match choice:
            case 1:
                print("\nRoute not made yet\n")
            case 2:
                print("\nRoute not made yet\n")
            case 3:
                genFight(player)
            case 4:
                print("\nRoute not made yet\n")
            case 5:
                run = False

player_name = input("What is your name\n: ")
print(f"Your name is {player_name}! \nYour options for starter pokemon are:")
print("""
Option 1 is water-type squirtle
Option 2 is fire-type charmander
Option 3 is nature-type bulbasaur
""")

starter_pokemon = int(input(f"What is your choice, pick using the numbers 1-3\n(1-3): "))
match starter_pokemon:
    case 1:
        starter_pokemon = "squirtle"
    case 2:
        starter_pokemon = "charmander"
    case 3:
        starter_pokemon = "bulbasaur"


main(Player(player_name, starter_pokemon))