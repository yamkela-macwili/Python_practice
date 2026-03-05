# Number Guessing Game

A simple command-line Python game where the user attempts to guess a randomly generated number.

## Description

This program generates a random number between **1 and 10** and asks the user to guess it.
The game continues until the correct number is entered.

If the user enters invalid input (such as text or a number outside the range), the program displays an error message and prompts the user again.

## Features

* Random number generation using Python's `random` module
* Input validation using exception handling
* Continuous guessing until the correct number is entered
* Simple command-line interface

## Requirements

* Python 3.x

No external libraries are required.

## How to Run

Clone the repository and navigate to the project folder:

```bash
git clone https://github.com/yamkela-macwili/Python_practice.git
cd Python_practice/00_fundamentals/number_guessing
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
Please enter your guess number (1 - 10): 4

Incorrect guess.
Try again.

Please enter your guess number (1 - 10): 7

Your guess is correct.
```

## Concepts Practiced

* Python functions
* While loops
* Conditional statements
* Exception handling
* User input handling
* Random number generation
