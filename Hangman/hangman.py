import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) #Random Word from this list
    if str(word) == 'zimmerman' or 'rai':
        print('ayo')
        word = random.choice(words) 
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.lower()

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
    word_letters = list(word)
    alphabet = set(string.ascii_lowercase)
    used_letters = set() # letters that users already guessed
    i = 1
    # user input
    while len(word_letters) > 0:
        #hangman picture
        print(hang[i])
        #to make sure that the final picture is printed before it breaks
        if i == 6:
            break

        # showing letters used after the first input
        if i > 1:    
            print('You have used these letters: ', ' '.join(used_letters))

        # what current word is
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print("Current word : ", " ".join(word_list))

        user_guess = input('Guess a letter: ').lower()
        if user_guess in alphabet - used_letters:
            used_letters.add(user_guess)     
            if user_guess not in word_letters:
                i += 1
            if user_guess in word_letters:
                word_letters.remove(user_guess)
        elif user_guess in used_letters:
            print("You have alzheimer?")
        else:
            print("Write something valid")
        print(" ")

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
