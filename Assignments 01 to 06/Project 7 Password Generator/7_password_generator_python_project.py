# Password Generator Python Project
# In this Code With Tomi tutorial, you will learn how to build a random password generator. 
# You will collect data from the user on the number of passwords and their lengths
#  and output a collection of passwords with random characters.
# This project will give you more practice working with for loops and the 
# random Python module.

import random
import string

def generate_password(length):
    """Creates a secure random password with the specified length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def main():
    try:
        num_passwords = int(input("How many passwords do you need? "))
        length = int(input("Specify the length of each password: "))

        print("\n🔐 Your Generated Passwords:")
        for _ in range(num_passwords):
            print(generate_password(length))

    except ValueError:
        print("⚠ Error: Please enter a valid number!")

if __name__ == "__main__":
    main()
