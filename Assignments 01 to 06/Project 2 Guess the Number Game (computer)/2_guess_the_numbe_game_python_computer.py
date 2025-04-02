# Guess the Number Game Python Project (computer)
# In this Kylie Ying tutorial, you will learn how to work with Python's 
# random module, build functions, work with while loops and conditionals,
#  and get user input.

import random

def number_guessing_game():
    print("🎯 Welcome to the Number Guessing Game!")

    for _ in range(5):  # Runs exactly 5 times
        target_number = random.randint(1, 100)
        tries = 0

        while True:
            guess = int(input("Guess a number (1-100): "))
            tries += 1

            if guess < target_number:
                print("Too low! Try again.")
            elif guess > target_number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Correct! You guessed it in {tries} tries.")
                break

# Run the game
if __name__ == "__main__":
    number_guessing_game()
