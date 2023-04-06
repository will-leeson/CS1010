import pygame
import sys
import random
import numpy as np
from gui import *

def init_game(word_file_loc):
    # TODO: Read in words from the text file into a list
    wordlist = []
    word_file = open(word_file_loc)
    for line in word_file:          # Read each line in the file
        wordlist.append(line.strip())  # Add the line to the word list (without newlines)

    # TODO: Randomly select and return a word from the word list
    word = np.random.choice(wordlist)
    return wordlist, word


def eval_guess(word, guess):
    print(word)
    evaluation = ""
    misses = []
    unmatched_word = ""
    unmatched_guess = ""
    for i, (letter_word, letter_guess) in enumerate(zip(word,guess)):
        if letter_word == letter_guess:
            evaluation+="$"
        else:
            unmatched_word += letter_word
            unmatched_guess += letter_guess
            evaluation+="#"
            misses.append(i)

    for i,letter_guess in zip(misses,unmatched_guess):
        if letter_guess in unmatched_word:
            evaluation = evaluation[:i] + "*" + evaluation[i+1:]
            unmatched_word = unmatched_word.replace(letter_guess, "_", 1)
    
    return evaluation


def checkValidInput(current_guess_string, wordlist):
    # TODO: Check if the current guess is in the list of words
    check1 = current_guess_string in wordlist

    # TODO: Check if the current guess is 5 characters long
    check2 = len(current_guess_string) == 5

    # TODO: Return True if both of the above are satisfied, False otherwise
    return check1 and check2


def main():
    file_path = "./words.txt"
    wordlist, word = init_game(file_path)
    runner(wordlist, word)

if __name__ == '__main__':
    main()