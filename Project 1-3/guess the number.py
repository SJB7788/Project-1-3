import random
from tracemalloc import start 

def startUp():
    while True:
        startGame = input("Which game would you like to play? Enter user guess, computer guess, or type q to quit: ").lower()
        if startGame == "user guess":
            userGuess()
            break
        if startGame == "computer guess":
            computerGuess_ready()
            break
        if startGame == "q":
            print("See you next time")
            break
        else: 
            print("Response is invalid!")
            continue

def userGuess():
    answer = random.randint(1, 100)
    guess = int(input("Guess the number between 1-100: "))
    while True:
        if guess > answer:
            print("Too High")
            guess = int(input("Guess again: "))
            continue
        if guess < answer:
            print("Too Low")
            guess = int(input("Guess again: "))
            continue
        if guess == answer:
            print("You got the right answer!")
            break
        
def computerGuess_ready():
    while True:
        ready = input("Choose a number between 1-100 and I will guess. Are you ready?: (Y/N): ").upper()
        if ready == "N":
            print("Lmao too bad")
            computerGuess()
            break
        if ready == "Y":
            computerGuess()
            break
        else: 
            print("Invalid Response")
            continue

def computerGuess():
    lowGuess = 1
    highGuess = 100
    def cRandom():
            global cGuess
            cGuess = random.randint(lowGuess, highGuess) 
            print(f"My guess is {cGuess}")
    cRandom()
    while True:
        answer = input("Is the number correct (C), too high (H), or too low (L)?: ").upper()
        if answer == "C":
            print("Too smart I am")
            break
        if answer == "H":
            highGuess = cGuess - 1 
            cRandom()
            continue
        if answer == "L":
            lowGuess = cGuess + 1
            cRandom()
            continue
        else: 
            print("Invalid Answer!")
            continue

startUp()
