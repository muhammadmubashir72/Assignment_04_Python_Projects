# Mad libs Python Project
# In this Kylie Ying tutorial, you will learn how to get input from the user, work with f-strings, and see your results printed to the console.

# This is a great starter project to get comfortable doing string concatenation in Python.

def fun_story():
    # Taking inputs for the story
    name = input("Enter a name: ")
    place = input("Enter a place: ")
    animal = input("Enter an animal: ")
    action = input("What was the animal doing? ")
    food = input("Enter a type of food: ")
    reaction = input("How did the person react? ")

    # Story Template
    story = f"""
    One day, {name} went to {place}. While walking around, they saw a {animal}.
    The {animal} was {action}, which made {name} very surprised!

    Without thinking, {name} threw a {food} at the {animal}.
    The {animal} looked confused and ran away. {name} just {reaction} and laughed.

    What a funny day at {place}!
    """

    # Printing the final story
    print("\nHere is your Mad Lib story:\n")
    print(story)

# Running the function
if __name__ == "__main__":
    fun_story()
