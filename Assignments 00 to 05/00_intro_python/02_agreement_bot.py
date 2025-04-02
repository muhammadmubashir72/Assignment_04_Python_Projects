## Problem Statement 2

# Write a program which asks the user what their favorite animal is, 
# and then always responds with "My favorite animal is also ___!" 
# (the blank should be filled in with the user-inputted animal, of course).
# Asking the user for their favorite animal

def main():
   favorite_animal = input("What's your favorite animal? ")

# Responding with the same animal
   print(f"My favorite animal is also {favorite_animal}!")

if __name__ == '__main__':
    main()
