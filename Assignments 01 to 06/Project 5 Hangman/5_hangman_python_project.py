# Hangman Python Project
# In this Kylie Ying tutorial, you will learn how to work with dictionaries, 
# lists, and nested if statements. You will also learn how to work with the 
# string and random Python modules.
import random

words = ["python", "developer", "hangman", "programming", "computer"]

def play():
    word = random.choice(words)
    guessed, attempts = set(), 6
    print("🎩 Welcome to Hangman! Guess the word. 🔤")

    while attempts > 0:
        print("\nWord:", " ".join([c if c in guessed else "_" for c in word]))
        print(f"Remaining attempts: {attempts}")

        guess = input("Guess a letter: ").lower()
        if not guess.isalpha() or len(guess) != 1 or guess in guessed:
            print("⚠ Invalid or repeated guess!")
            continue

        guessed.add(guess)
        if guess not in word:
            attempts -= 1
            print("❌ Incorrect!")

        if all(c in guessed for c in word):
            print(f"🎉 You guessed it! The word was: {word}")
            return

    print(f"💀 Game Over! The word was: {word}")

if __name__ == "__main__":
    play()

