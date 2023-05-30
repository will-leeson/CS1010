'''
Name: Erlin Sorto
Computing ID: Els5jsx
Collaborators: n/a
Resources: https://www.w3schools.com/python/python_dictionaries.asp
https://www.w3schools.com/python/ref_random_choice.asp
'''

import pygame
import sys
import random
import numpy as np
from gui import *

def init_game(word_file_loc):
    word_file = open(word_file_loc)
    wordlist = []
    for line in word_file:
        word = line.strip()
        wordlist.append(word)

    # TODO: Randomly select and return a word from the word list
    # Hint: random.shuffle(a_list) will shuffle a_list
    word = random.choice(wordlist)
    return wordlist, word


def checkValidInput(current_guess_string, wordlist):
    # TODO: Check if the current guess is in the list of words
    # TODO: Check if the current guess is 5 characters long
    if current_guess_string in wordlist and len(current_guess_string) == 5:
        return True
    # TODO: Return True if both of the above are satisfied, False otherwise


    return False

def eval_guess(word, guess):
    # This string will tell them how they did.
    # Incorrect character (#)
    # Correct character, incorrect spot (*)
    # Correct character, correct spot ($)
    # Example: If the word if "pulls" and the user guesses "plump", the evaluation string should be $**##
    evaluation = ["#"] * 5
    usedWords = {}
    for x in word:
        if x in usedWords:
            usedWords[x]+=1
        else:
            usedWords[x] = 1
    for x in range(len(guess)):
        if guess[x] == word[x]:
            evaluation[x] = "$"
            usedWords[guess[x]] -=1
    for x in range(len(guess)):
        currval = guess[x]
        if currval in word and usedWords[currval] > 0 and evaluation[x] != "$":
            evaluation[x] = "*"
            usedWords[guess[x]] -= 1

    
    

    # TODO: Check for when the guess and word match  
    # Hint: You can loop through the letters in a string
    # Hint: you can loop through two things at once with the "zip" command

    # TODO: Check for when the guess has letters that don't match exactly, but are in the word
    # Hint: Use helper variables in the previous loop to keep track of letters that didn't match 

    return ''.join(evaluation)



def main():
    file_path = "./words.txt"
    wordlist, word = init_game(file_path)
    runner(wordlist, word)

if __name__ == '__main__':
    main()
