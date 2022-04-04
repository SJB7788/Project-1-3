import random
from turtle import left
from words import words
import string

def get_valid_word(words):
    word = random.choices(words) #Random Word from this list
    while '-' in word or ' ' in word:
        word = random.choice(word)
    
    return word 

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_lowercase)
    used_letters = set() # letters that users already guessed
    print(word)

    # user input
    while len(word_letters) > 0:
        # letters used
        print('You have used these letters: ', ' '.join(used_letters))
    
        # what current word is
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word : ", " ".join(word_list))

        user_guess = input('Guess a letter: ').lower()
        if user_guess in alphabet - used_letters:
            used_letters.add(user_guess)
            if user_guess in word_letters:
                word_letters.remove(user_guess)
        elif user_guess in used_letters:
            print("You have alzheimer?")
        else:
            print("Write something valid")
        

hangman()