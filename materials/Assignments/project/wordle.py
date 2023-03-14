from typing import Tuple
import numpy as np

def game_setup(word_file_loc: str) -> str:
    words = []
    word_file = open(word_file_loc)
    for line in word_file:          # Read each line in the file
        words.append(line.strip())  # Add the line to the word list (without newlines)

    word = np.random.choice(words)

    return word

def eval_guess(word: str, guess:str) -> str:
    evaluation = ""
    misses = []
    unmatched_word = ""
    unmatched_guess = ""
    for i, (letter_word, letter_guess) in enumerate(zip(word,guess)):
        if letter_word == letter_guess:
            evaluation+=letter_guess
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

def game_loop(word: str) -> int:
    num_guesses = 0

    print("The word has " + str(len(word)) + " letters.") 
    guess = None

    while guess != word:
        guess = input("Make a guess: ")
        if len(guess) != len(word):
            print("Your guess is", len(guess), "letters and the word is", len(word), "letters. Try again.")
            continue

        eval = eval_guess(word=word, guess=guess)
        print(eval)
        num_guesses+=1

    return num_guesses

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