from typing import Tuple
import numpy as np

def game_setup(word_file_loc: str) -> str:
    words = []
    word_file = open(word_file_loc)
    
    # TODO: Read each line in the file
    #       Add the line to the list words (without newlines)

    word = np.random.choice(words)

    return word

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

    print("The word has " + str(len(word)) + " letters.") 
    guess = None

    while guess != word:
        guess = input("Make a guess: ")
        
        # TODO: Check that guess has the same number of letters as the word
        #       If this isn't the case, tell them and have them make another guess

        eval = eval_guess(word=word, guess=guess)

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

    word = game_setup(word_file_loc="test.txt")

    num_guesses = game_loop(word)
    print("It took you", num_guesses, "tries")



if __name__ == "__main__":
    main()