# Guess the Number Game Python Project (user)
# In this Kylie Ying tutorial, you will build a guessing game where the computer 
# has to guess the correct number. You will work with Python's random module,
#  build functions, work with while loops and conditionals, and get user input.

import random

def computer_guesses():
    print("🎯 Welcome to the Number Guessing Game!")
    print("Think of a number between 1 and 100, and I will guess it.")

    low, high = 1, 100
    attempts = 0

    while low <= high:
        guess = (low + high) // 2  # More optimized guessing
        attempts += 1
        
        print(f"Is your number {guess}?")
        user_feedback = input("Enter 'h' if too high, 'l' if too low, or 'c' if correct: ").lower()

        if user_feedback == "h":
            high = guess - 1
        elif user_feedback == "l":
            low = guess + 1
        elif user_feedback == "c":
            print(f"🎉 I guessed your number {guess} in {attempts} tries!")
            break
        else:
            print("⚠️ Invalid input! Please enter 'h', 'l', or 'c'.")

if __name__ == "__main__":
    computer_guesses()
