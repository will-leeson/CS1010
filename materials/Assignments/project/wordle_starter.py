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
    word = ""

    return wordlist, word


def eval_guess(word, guess):
    # This string will tell them how they did.
    # Incorrect character (#)
    # Correct character, incorrect spot (*)
    # Correct character, correct spot ($)
    # Example: If the word if "pulls" and the user guesses "plump", the evaluation string should be $**##

    evaluation = ""

    # TODO: Check for when the guess and word match  
    # Hint: You can loop through the letters in a string
    # Hint: you can loop through two things at once with the "zip" command

    # TODO: Check for when the guess has letters that don't match exactly, but are in the word
    # Hint: Use helper variables in the previous loop to keep track of letters that didn't match 

    return evaluation


def checkValidInput(current_guess_string, wordlist):
    # TODO: Check if the current guess is in the list of words

    # TODO: Check if the current guess is 5 characters long

    # TODO: Return True if both of the above are satisfied, False otherwise

    return False


def main():
    file_path = "./words.txt"
    wordlist, word = init_game(file_path)
    runner(wordlist, word)

if __name__ == '__main__':
    main()