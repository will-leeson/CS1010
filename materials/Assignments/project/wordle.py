'''
Name: Katherine Frier
Computing ID: Svt8xq
Collaborators: Skylar Mullins
Resources:
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
    secret_word=wordlist[random.randint(0,len(wordlist))]
    word=secret_word
    print(word)

    # TODO: Randomly select and return a word from the word list
    # Hint: random.shuffle(a_list) will shuffle a_list
    

    return wordlist, word

def checkValidInput(current_guess_string, wordlist):
    word_guess=current_guess_string
    # TODO: Check if the current guess is in the list of words
    if len(word_guess)==5 and word_guess in wordlist:
        return True 
    else:
        return False 

    # TODO: Check if the current guess is 5 characters long

    # TODO: Return True if both of the above are satisfied, False otherwise


def eval_guess(word, guess):
    global word_list

    # This string will tell them how they did.
    # Incorrect character (#)
    # Correct character, incorrect spot (*)
    # Correct character, correct spot ($)
    # Example: If the word if "pulls" and the user guesses "plump", the evaluation string should be $**##
    evaluation =""
    guesslist=[]
    i=0
    if guess==word:
        evaluation="$$$$$"
    else:
        for letter in guess:
            if letter in guesslist:
                if letter in word[i:]:
                    if guess[i]==word[i]:
                        evaluation+="$"
                        i+=1
                        guesslist.append(letter)
                elif guess[i]!=word[i] and letter in word[i:]:
                        evaluation+="*"
                        i+=1
                        guesslist.append(letter)
                elif letter not in word[i:]:
                    evaluation+="#"
                    i+=1
                    guesslist.append(letter)
            elif letter not in guesslist:
                if letter in word and guess[i]==word[i]: 
                    evaluation+="$"
                    i+=1
                    guesslist.append(letter)
                elif letter in word and guess[i] != word[i]:
                    evaluation+="*"
                    i+=1
                    guesslist.append(letter)
                elif letter not in word:
                    evaluation+="#"
                    i+=1
                    guesslist.append(letter)

                



    # TODO: Check for when the guess and word match  
    # Hint: You can loop through the letters in a string
    # Hint: you can loop through two things at once with the "zip" command

    # TODO: Check for when the guess has letters that don't match exactly, but are in the word
    # Hint: Use helper variables in the previous loop to keep track of letters that didn't match 

    return evaluation



def main():
    global secret_word
    file_path = "./words.txt"
    wordlist, word = init_game(file_path)
    runner(wordlist, word)

if __name__ == '__main__':
    main()