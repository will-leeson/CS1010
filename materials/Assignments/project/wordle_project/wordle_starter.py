from typing import Tuple
from random import choice

def game_setup(word_file_loc: str) -> str:
    words = []
    word_file = open(word_file_loc)
    
    # Loop through each line in the file
    for line in word_file:
        # We need to strip the "enter" character at the end
        words.append(line.strip())

    # TODO: Randomly selects a word
    # Hint: The choice function imported at the top of this file
    #       randomly selects an item in a list
       
    
    # TODO: Return the word at the end of the function


def eval_guess(word: str, guess:str) -> str:
    # This string will tell them how they did
    evaluation = ""

    # TODO: Check for when the guess and word match  
    # Hint: You can loop through the letters in a string
    # Hint: you can loop through two things at once with the "zip" command

    # TODO: Check for when the guess has letters that don't match exactly, but are in the word
    # Hint: Use helper variables in the previous loop to keep track of letters that didn't match 


    return evaluation

def game_loop(word: str) -> int:
    num_guesses = 0

    guess = None

    while guess != word:
        
        guess = ""
        
        # TODO: Check that guess has 5 letters
        #       If this isn't the case, tell them and have them make another guess
        #       If it is the case, evaluate the guess using the eval 

        eval = eval_guess(word=word, guess=guess)
        print(eval)

    # TODO: Return the number of times they guessed

def main():
    print("=============================================")
    print("Welcome to Wordle!")
    print("Here is how the game works, I will choose")
    print("a word. I will tell you how many letters")
    print("are in the word. You then have to guess")
    print("the word. If you get a letter in the right")
    print("spot, I'll let you know. If you guess a")
    print("letter thats in the word, but in the wrong")
    print("spot, I'll let you know as well. Try to guess")
    print("the word in the least amount of guesses.")
    print("=============================================")
    print()

    word = game_setup(word_file_loc="words.txt")

    num_guesses = game_loop(word)
    print("It took you", num_guesses, "tries")



if __name__ == "__main__":
    main()