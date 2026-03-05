# Character Guessing Game

A simple command-line Python game where the user attempts to guess the letters of a randomly chosen word.

## Description

This program selects a random word from a predefined list and asks the user to guess its letters one by one.
The word is displayed as underscores `_` for unknown letters and fills in correctly guessed letters.
The game continues until all letters are guessed.

If the user enters invalid input (such as numbers, multiple letters, or an empty input) or repeats a guess, the program displays an error message and prompts the user again.

## Features

* Random word selection from a predefined list
* Character-by-character guessing
* Input validation using exception handling
* Tracks already guessed letters to prevent duplicates
* Displays word progress visually
* Simple command-line interface

## Requirements

* Python 3.x

No external libraries are required.

## How to Run

Clone the repository and navigate to the project folder:

```bash
git clone https://github.com/yamkela-macwili/Python_practice.git
cd Python_practice/00_fundamentals/word_guessing
```

### Linux / macOS

```bash
python3 main.py
```

### Windows

```bash
python main.py
```

## Example

```
Enter your username: Yamkela
Good Luck Yamkela!

The word has 7 characters.

Word: _ _ _ _ _ _ _
Guess a character: h
Good guess! 'h' is in the word.

Word: h _ _ _ _ _ _
Guess a character: a
Good guess! 'a' is in the word.

Word: h a _ _ _ a _
Guess a character: n
Good guess! 'n' is in the word.

Word: h a n _ _ a n
...
Congratulations Yamkela! You guessed the word: 'hangman'.
```

## Concepts Practiced

* Python functions
* While loops
* Conditional statements
* Exception handling
* User input handling
* Random word selection
* Game logic


