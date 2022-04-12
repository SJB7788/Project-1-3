import time
from tracemalloc import start

question = [
    "What is 1 + 1: ",
    "What gets wet while drying?: ",
    "I shave every day, but my beard stays the same. What am I?: ",
    "What building has the most stories?: ",
    "What word is always spelled wrong?: ",
    'Quick, write "yes": ',
    "Break it and it gets better; set it and it's harder to break. What am I?: ",
    "The more of this there is, the less you see. What is it?: ",
    "Should you run a red light?: ",
    "Does the person who made this quiz want to go home?: ",
]

answer = [
    "two",
    "towel",
    "barber",
    "library",
    "wrong",
    "yes",
    "record",
    "darkness",
    "no",
    "yes"
]

def startQuiz():
    while True:
        bootUp = input("Would you like to be quizzed?: ").lower()
        if bootUp == "yes":
            time.sleep(1)
            quiz()
            break
        if bootUp == "no":
            print("Good Bye")
            break
        else:
            print("Invalid Answer")
            continue

def quiz():
    global score
    score = 0
    wrongStreak = 0
    
    print("\nNote: when answering questions, answer in one word. Do not add 'A' or 'The' in your answers.")
    time.sleep(3)
    print("\nWelcome to the quiz")
    print("Hopefully there are no bugs and things go smoothly. Please give me full marks -anonymous \n")
    time.sleep(3)
    
    for i in range(len(question)):
        if i == 5:
            #setting a time 
            time1 = time.time()
            userAnswer = input(question[i])

            #setting a time after the answer
            time2 = time.time()
            
            #subtracting the inital time and final time to see if it took 2 seconds to answer
            totalTime = time2 - time1
            print(str(totalTime) + 's')
            if int(totalTime) == 0 and userAnswer == answer[i]:
            #because its int, it will round down so tehcnically the user has 1 second to respond
                print("Good Reaction Time\n")
                time.sleep(1)
                continue
            if totalTime > 1:
                print("Tsk tsk, Too Slow\n")
                time.sleep(1)
                continue
            else: 
                print("Wrong")
                continue
        userAnswer = input(question[i])
        if userAnswer == answer[i]:
            score += 1
            wrongStreak = 0
            print("Score: " + str(score) + "\n")
        else:
            print("wrong\n")
            wrongStreak += 1
            if wrongStreak == 5:
                print("Damn you got 5 wrong in a row. Impressive\n")
        time.sleep(1)
    
    endScreen()
    

def endScreen():
    print("Final Score: " + str(score))
    while True:
        replay = input("Play Again? (Y/N): ").upper()
        if replay == "Y":
            quiz()
        if replay == "N":
            print("Good Bye")
            break
        else:
            print("Invalid Response")
            continue

startQuiz()