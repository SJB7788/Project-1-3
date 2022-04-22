from types import new_class
from PIL import Image
import time

# starting screen
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
    while True:
        userStart = input("").upper()
        if userStart == "P":
            print("\nStarting Game....\n")
            time.sleep(3)
            textRPG()
            break
        if userStart == "Q":
            print("Good Bye")
            break
        else:
            print("Invalid Input")
            continue

# useless text to lower expectations
def textRPG():
    global name
    print("This game is only a tech demo and only contains the combat sequence\n")
    time.sleep(2)
    name = input("Player's Name: ")
    print(f"{name} have encountered a slime!\n")
    time.sleep(1)
    fightSequence()

# function name should be straightforward
def fightSequence():
    # open image of a slime from dragon quest
    slimePNG = Image.open(r"Project Set\Slime_(Dragon_Quest).png")
    slimePNG.show()
    # mob class to make any type of mob
    class mob:
        def __init__(enemy, name, health, ATK, DEF, LVL):
            enemy.name = name
            enemy.health = health
            enemy.ATK = ATK
            enemy.DEF = DEF
            enemy.LVL = LVL
    # user stat lvl at lvl 1
    statLvl = {
        "Helmet": 1,
        "Chestplate": 1,
        "Boots": 1,
        "Sword": 1,
        "ATK": 10,
        "DEF": 10,
        "Health": 100,
        "Speed": 5,
        "LVPoints" : 100
    }
    # stat screen in a list so I can update the string later (bugged idk whats wrong with this actually)
    stat = [
        " ____________________________________________ ",
        "|             Character Profile              |",
        "| ▯ Helmet (LV." + str(statLvl["Helmet"]) +
        ") + H       LV. Points: "+ str(statLvl["LVPoints"]) +"  |",
        "| ▯ Chestplate (LV." +
        str(statLvl["Chestplate"]) + ") + C                    |",
        "| ▯ Boots (LV." + str(statLvl["Boots"]) +
        ") + B                         |",
        "| ------------------------------------------ |",
        "| ▯ Sword (LV." + str(statLvl["Sword"]) +
        ") + S                         |",
        "| ------------------------------------------ |",
        "| Stats:                                     |",
        "|   ATK: " + str(statLvl["ATK"]) + "                                  |",
        "|   DEF: " + str(statLvl["DEF"]) + "                                  |",
        "|   Health: " + str(statLvl["Health"]) + "                              |",
        "|   Speed: " + str(statLvl["Speed"]) + "                                 |",
        "|____________________________________________|"
    ]
    
    slime = mob("Slime", 20, 10, 0, 1)  # creating a new mob which is a slime
    # Enemy attack function to not flood the code with the same shiz
    def enemyATK():
            time.sleep(1)
            print("The slime attacks!")
            time.sleep(0.5)
            print(f"It dealt {slime.ATK} to {name} health!\n")
            statLvl["Health"] -= slime.ATK
    # the actual fight sequence
    while True:
        # health == 0 => game over
        if statLvl["Health"] <= 0:
            time.sleep(1)
            print(f'{name} Health: {statLvl["Health"]}')
            time.sleep(1)
            print(f"{name} really lost to a slime. {name} should be ashamed")
            time.sleep(1)
            print("Game Over")
            break
        time.sleep(1)
        # print name of the enemy, the lvl, enemy health and the players health
        print(f'{slime.name} LVL.{slime.LVL} \nEnemy Health: {slime.health}\n\nYour Health: {statLvl["Health"]}\n')
        time.sleep(1)
        userFightInput = input(
            "You have these options:\nA(Attack), S(Stats), R(Run): ").upper()
        if userFightInput == "A":
            time.sleep(1)
            print(f"\n{name} hit the slime")
            time.sleep(1)
            print(f"\n{name} dealt " +
                  str(statLvl["ATK"]) + " Damage to the slime\n")
            slime.health = slime.health - statLvl["ATK"]
            if slime.health <= 0:
                time.sleep(1)
                print(f"{name} have defeated the slime!")
                break
            enemyATK()
            continue
        if userFightInput == "S":
            # i dont know why it doesnt update the stat screen. i tested it and it changes the dictionary value just not 
            # the stat screen. might have to do with the fact that the stat screen bases off of the original dictionary
            # not the one that is updated during the if statement sad

            # now that I think about it i probably shouldve just made the user's stat into a class and updated it that way
            # it worked for the slime fight sequence so maybe it wouldve worked with the user's stat screen
            while True:
                for i in stat:
                    print(i)
                statUpgrade = input("H: Helmet, C: Chestplate, B: Boots, S: Sword, Q: Back to fight\n").upper()
                if statUpgrade == "H":
                    statLvl["Helmet"] += 1
                    statLvl["Health"] += 50
                    continue
                if statUpgrade == "C":
                    statLvl["Chestplate"] += 1
                    statLvl["DEF"] += 10
                    continue
                if statUpgrade == "B":
                    statLvl["Boots"] += 1
                    statLvl["Speed"] += 5
                    continue
                if statUpgrade == "S":
                    statLvl["Sword"] += 1
                    statLvl["ATK"] += 10
                    continue
                if statUpgrade == "Q":
                    print("")
                    break
            continue
        if userFightInput == "R":
            print("\nFight the slime wuss\n")
            enemyATK()
            continue
        else:
            print("Invalid Input\n")

textRPGStart()