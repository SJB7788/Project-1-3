import random
from tkinter import N

def start():
    while True:
        choice = input("Play game? (P) or Quit (Q): ")
        if choice == 'P':
            gameStart()
            break
        if choice == 'Q':
            print("Good Bye")
            break
        else:
            print("That is not a valid input")
            continue

def gameStart():
    wincount = 0
    lostcount = 0
    while True:
        userChoice = input("Rock (R), Paper (P), Scissors (S), Lizard (L), Spock (Sp)?  [Q to Quit]:\n")
        computerChoice = random.choice(['R', 'P', 'S', 'L', 'Sp'])

        if userChoice == 'Q':
            print("Good Bye")
            break
        
        print(computerChoice)
        
        if (userChoice == 'R' and computerChoice == 'S') or (userChoice == 'S' and computerChoice == 'P') or (userChoice == 'P' and computerChoice == 'R') \
            or (userChoice == 'L' and computerChoice == 'Sp') or (userChoice == 'Sp' and computerChoice == 'S') or (userChoice == 'P' and computerChoice == 'Sp') \
                or (userChoice == 'Sp' and computerChoice == 'R') or (userChoice == 'L' and computerChoice == 'P') or (userChoice == 'S' and computerChoice == 'L'):
                print("You Won! ")
                wincount += 1
                print("Win count: " + str(wincount))
                continue

        if (userChoice == computerChoice):
            print("Tie")
            continue

        else: 
            print("YOU LOST")
            lostcount += 1
            print('Lose count: ' + str(lostcount))
            continue

start()
