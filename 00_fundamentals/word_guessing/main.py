"""
Character Guessing Game (Mini Hangman)

This module implements a command-line game where the user tries to guess
the letters of a randomly chosen word. The word is displayed as underscores
for unknown letters and fills in letters as the user guesses correctly.

Features:
- Random word selection
- Character-by-character guessing
- Input validation
- Tracks already guessed letters
- Displays progress visually
"""
from random import choice

def main(): 
    words = [
        "python", 
        "hangman", 
        "developer", 
        "computer", 
        "keyboard",
        "algorithm",
        "function",
        "variable",
        "iteration",
        "exception",
        "programming",
        "terminal"
    ]
    while True:
        try:
            name = input("Enter your username: ")
            if not name:
                raise ValueError
            if len(name) < 3:
                raise ValueError
            print(f"Good Luck {name.capitalize()}!\n")
            break
        except ValueError as e:
            print("Please provide a valid username, at least 3 characters long.")

    word = choice(words)
    guessed_chars = set()
    display_word = ["_"] * len(word)

    print(f"The word has {len(word)} characters.\n")

    while "_" in display_word:
        try:
            print("Word: " + " ".join(display_word))
            guess = input("Guess a character: ").lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single alphabet character.\n")
                continue
            if guess in guessed_chars:
                print(f"You already guessed '{guess}'. Try another.\n")
                continue
            
            guessed_chars.add(guess)
            if guess in word:
                print(f"Good guess! '{guess}' is in the word.\n")
                for i, char in enumerate(word):
                    if char == guess:
                        display_word[i] = guess
            else:
                print(f"'{guess}' is not in the word. Try again.\n")

            print(f"Congratulations {name.capitalize()}! You guessed the word: '{word}'.")
        except Exception as e:

            print(e)

if __name__=="__main__":
    main()