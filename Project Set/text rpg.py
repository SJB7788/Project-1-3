from types import new_class
from PIL import Image  
import time 






def textRPGStart():
    print(     
    """
    ______________________________________________
    |                 Text RPG                   |
    |                                            |
    |      Play(P)                 Quit(Q)       |
    |____________________________________________|
    """
        )
    userStart = input("").upper()
    while True:
        if userStart == "P":
            print("Starting Game....\n")
            textRPG()
            break
        if userStart == "Q":
            print("Good Bye")
            break
        else:
            print("Invalid Input")

def textRPG():
    print("This game is only a tech demo and only contains the combat sequence\n")
    time.sleep(1)
    print("You have encountered a slime")
    
def fightSequence():
    class mob:
        def __init__(enemy, name, health, ATK, DEF):
            enemy.name = name
            enemy.health = health
            enemy.ATK = ATK
            enemy.DEF = DEF

    statLvl = {
        "Helmet": 1, 
        "Chestplate": 1, 
        "Boots": 1, 
        "Sword": 1,
        "ATK": 10,
        "DEF": 10,
        "Health": 100,
        "Speed": 5
    }

    stat = [
        " ____________________________________________ ",
        "|             Character Profile              |",
        "| ▯ Helmet (LV." + str(statLvl["Helmet"]) + ")          LV. Points: 0     |",
        "| ▯ Chestplate (LV." + str(statLvl["Chestplate"]) + ")                        |",
        "| ▯ Boots (LV." + str(statLvl["Boots"]) + ")                             |",
        "| ------------------------------------------ |",
        "| ▯ Sword (LV." + str(statLvl["Sword"]) +")                             |",
        "| ------------------------------------------ |",
        "| Stats:                                     |",
        "|   ATK: 10                                  |",
        "|   DEF: 10                                  |",
        "|   Health: 100                              |",
        "|   Speed: 5                                 |",
        "|____________________________________________|"
    ]
    
    slime = mob("Slime", 20, 5, 0) #creating a new slime class

    while True:
        userFightInput = input("You have these options:\nA(Attack), S(Stats), R(Run): ").upper()
        if userFightInput == "A":
            time.sleep(1)
            print("\nYou hit the slime")
            time.sleep(1)
            print("\nYou dealt " + str(statLvl["ATK"]) + " Damage to the slime")
            slime.health = slime.health - statLvl["ATK"]
            print("Slime Health: " + str(slime.health))
            if slime.health == 0:
                print("You have defeated the slime!")
                break
            continue
        if userFightInput == "S":
            for i in stat:
                print(i)
            continue
        if userFightInput == "R":
            print("\nFight the slime wuss\n")
            continue
        else: print("Invalid Input\n")

    

fightSequence()