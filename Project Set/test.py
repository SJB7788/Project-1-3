from PIL import Image
import time

test = Image.open(r"Project Set\Slime_(Dragon_Quest).png")
test.show()

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

for i in stat:
    print(i)
statUpgrade = input("H: Helmet, C: Chestplate, B: Boots, S: Sword, Q: Back to fight\n").upper()
if statUpgrade == "H":
    statLvl["Helmet"] += 1
    statLvl["Health"] += 50
print(statLvl)
for i in stat:
    print(i)
print(statLvl["Health"])
print(stat[2])