import random as ran
import string as st
from words2 import words
from usedWords import used_words
#from words2 import words2
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
        

        user_letter=input("Guess a letter: ").upper()
        if user_letter in alphabet:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives=lives-1
        elif user_letter in used_letters:
            print("Already used that letter.Try again")
        else:
            print("Invalid Input")
    if len(word_letters)==0:
        print("Congratulations!! You've guessed the right word")
        print(word)
    else:
        print("Better luck next time kid")
        print(word)
    used_words.append(word)
    print(used_words)
        
        #print(alphabet)
hangman()
