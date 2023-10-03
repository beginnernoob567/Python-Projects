import random as ran
import string as st
from words2 import words

def get_valid_word(words):
    word=ran.choice(words)
    while '-' in word or ' ' in word:
        word=ran.choice(words)
    return word.upper()

def hangman():
    word=get_valid_word(words)
    word_letters=set(word)
    alphabet=set(st.ascii_uppercase)
    used_letters=set()
    lives=6

    print("The word is - ",len(word),"letters long")
    while len(word_letters)>0 and lives>0:
        #used letters|
        print(f"You have {lives} lives left and You've used these letters: ",' '.join(used_letters))
        #current word
        for letter in word:
            if letter in used_letters:
                print(letter)
            else:
                print('-')
        print("Current word:",''.join(word_list))
hangman()
