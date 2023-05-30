'''
Name: Emily Hall
Computing ID: hhd8by
Collaborators:
Resources: https://stackoverflow.com/questions/66963784/using-the-zip-method-in-python-to-count-character-equality-in-2-strings-accordin
https://www.learndatasci.com/solutions/python-string-contains/#:~:text=The%20easiest%20and%20most%20effective,can't%20find%20the%20substring.
https://www.codecademy.com/learn/introduction-to-python-dvp/modules/python-syntax-dvp/cheatsheet
'''

import pygame #on my computer both the words pygame, sys, and np are a darker green than the other libraries, like they are greyed out and not working.
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
    random.shuffle(wordlist) #this would shuffle the world list
    word = wordlist.pop() #this will take the last word from the newly shuffled word list and set it equal to word
    return wordlist, word


def checkValidInput(current_guess_string, wordlist):
    # TODO: Check if the current guess is in the list of words
    # TODO: Check if the current guess is 5 characters long
    # TODO: Return True if both of the above are satisfied, False otherwise
    if current_guess_string in wordlist and len(current_guess_string) == 5: 
        return True #If both conditions are true, then it will return true
    else: return False #but if either is false it will return false

def eval_guess(word, guess):
    # This string will tell them how they did.
    # Incorrect character (#)
    # Correct character, incorrect spot (*)
    # Correct character, correct spot ($)
    # Example: If the word if "pulls" and the user guesses "plump", the evaluation string should be $**##
    evaluation = ""
    # TODO: Check for when the guess and word match  
    # Hint: You can loop through the letters in    a string
    # Hint: you can loop through two things at once with the "zip" command
    for i, x in zip(word, guess): #this would run through the two strings, i being the letters in word and x being the letters in guess
        if i == x: #if the letters in question are equal, then the evaluation string will have $ added, showing that the letter is correct there. 
            evaluation += "$" 
    # TODO: Check for when the guess has letters that don't match exactly, but are in the word
    # Hint: Use helper variables in the previous loop to keep track of letters that didn't match 
        elif x in word: #if the letter in question of the guess is in the word, then the evaluation string will have * added, showing that the letter is in the word, but not there.
            evaluation += "*"
        else: #if the letter in question of the guess doesn't math the letter of the word, nor it is in the word, then the evaluation string will have # added, showing that the letter is incorrect. 
            evaluation += "#" 
    return evaluation

def main():
    file_path = "./words.txt"
    wordlist, word = init_game(file_path)
    runner(wordlist, word)

if __name__ == '__main__':
    main()