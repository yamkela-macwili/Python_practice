"""
Simple Number Guessing Game.

This module implements a command-line guessing game where the user
tries to guess a randomly generated number between 1 and 10.
"""
from random import randrange

def main():
    """
    Run the number guessing game.

    The function generates a random number between 1 and 10 (inclusive)
    and repeatedly prompts the user to guess the number. The loop
    continues until the user guesses correctly.

    Handles invalid inputs by displaying an error message when the
    user enters a non-integer value.
    """
    actual_number = randrange(1, 11)
    while True:
        try:
            guess_number = int(input("Please enter your guess number (1 - 10): "))
            if not 1 <= guess_number <= 10:
                raise ValueError
            if guess_number == actual_number:
                print("\nYour guess is correct.\n")
                break
            print("\nIncorrect guess. \nTry again.\n")
        except ValueError as e:
            print("\nPlease only enter an interger number between 1 and 10\n")

if __name__ == "__main__":
    main()