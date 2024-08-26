"""
Number Guessing Game

A simple command-line game where the player tries to guess a random number between 1 and 100.

Features:
- Random number generation for each game
- Input validation
- Limited attempts (7) per game
- Informative feedback after each guess
- Option to play multiple rounds

Run this script to start the game.
"""

import random


def get_valid_input(prompt, min_val, max_val):
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def play_game():
    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    print("Welcome to the Number Guessing Game!")
    print(
        f"I'm thinking of a number between 1 and 100. You have {max_attempts} attempts."
    )

    while attempts < max_attempts:
        prompt = f"Attempt {attempts + 1}/{max_attempts}. Enter your guess: "
        guessed_number = get_valid_input(prompt, 1, 100)
        attempts += 1

        if guessed_number == number:
            print(f"Congratulations! You guessed the number in {attempts} attempts!")
            return True
        elif guessed_number < number:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")

    print(f"Sorry, you've run out of attempts. The number was {number}.")
    return False


def main():
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing. Goodbye!")
            break


if __name__ == "__main__":
    main()
