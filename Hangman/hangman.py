import random
import time
import string

words = ["jaw", "era", "death", "sandwich", "curtain", "nose", "elegant", "pedestrain", "epicalyx", "influence",   
    "uncanny", "strange", "stooge", "sunny", "house", "cream", "fountain", "stick", "license", "together", "clock",
    "love", "time", "zimmerman", "rai", "kwantlen"]

def get_valid_word(words):
    word = random.choice(words) #Random Word from this list
    while word == 'rai' or word == 'zimmerman': #removing zimmerman and rai from being the answer
        word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

hang = [ """
     + ===== +
     I       |
             |
             |
             |
             |
             |
    =========== 
    """,
    """
     + ===== +
     I       |
     O       |
             |
             |
             |
             |
    =========== 
    """,
    """
     + ===== +
     I       |
     O       |
     |       |
             |
             |
             |
    =========== 
    """,
    """
     + ===== +
     I       |
     O       |
     |\      |
             |
             |
             |
    =========== 
    """,
    """
     + ===== +
     I       |
     O       |
    /|\      |
             |
             |
             |
    =========== 
    """,
    """
     + ===== +
     I       |
     O       |
    /|\      |
    /        |
             |
             |
    =========== 
    """,
    """
     + ===== +
     I       |
     O       |
    /|\      | dead
    / \      |
             |
             |
    =========== 
    """,
    
]

def hangman():
    word = get_valid_word(words)
    print(word)
    word_letters = list(word)
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U'
    ,'V', 'W', 'X', 'Y', 'Z']
    used_letters = set() # letters that users already guessed
    i = 1
    # user input
    while len(word_letters) > 0:
        # hangman picture
        print(hang[i])

        # to make sure that the final picture is printed before it breaks
        if i == 6:
            break
        
        # showing letters used after the first input
        print(' '.join(alphabet))

        # what current word is
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print("Current word : ", " ".join(word_list))

        #user input
        user_guess = input('Guess a letter: ').upper()

        #updates the list of letters left
        if user_guess in alphabet:
            index = alphabet.index(user_guess)
            alphabet.remove(alphabet[index])
            alphabet.insert(index, '#')
            
            # adds user guess into used letter set 
            if user_guess not in used_letters:
                used_letters.add(user_guess)
            
            # when guessed wrong, it updates the count of i to update the hangman picture
            if user_guess not in word_letters:
                i += 1
                fail_phrases = ["Wrong, Terrible Guess", "WRONG", "Unique Message to inform you that you are wrong",
                "You Suck KEK", "I don't know how else to say you are wrong", "Current Rank: Plastic 5 (You Suck Basically)"]
                print(random.choice(fail_phrases))
            if user_guess in word_letters:
                word_letters.remove(user_guess)
                print("Lucky Guess")
        elif user_guess in used_letters:
            print("Used Letter")
        else:
            print("Write something valid")
        print(" ")

        time.sleep(1) #time delay by 1s

    print("Final word: " + word)
    play_request()

#function to ask whether to play again or not
def play_request():
    while True:
        request_a = input("Would you like to play again? (Y/N): ")
        if request_a == 'Y':
            hangman()
        if request_a == 'N':
            print("Good Bye")
            break
        else: 
            print("Invalid Answer")
            continue

hangman()
