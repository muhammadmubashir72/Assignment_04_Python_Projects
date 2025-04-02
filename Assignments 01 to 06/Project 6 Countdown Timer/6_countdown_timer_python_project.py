# Countdown Timer Python Project
# In this Code With Tomi tutorial, 
# you will learn how to build a countdown timer using the time Python module.
#  This is a great beginner project to get you used to working with while loops in Python.

import time

def start_timer(duration):
    """Initiates a countdown from the specified duration in seconds."""
    while duration > 0:
        minutes, seconds = divmod(duration, 60)
        print(f"{minutes:02d}:{seconds:02d}", end="\r")
        time.sleep(1)
        duration -= 1

    print("⏰ Time’s up! 🚀")

if __name__ == "__main__":
    try:
        time_input = int(input("Set countdown time (seconds): "))
        start_timer(time_input)
    except ValueError:
        print("❌ Invalid input! Please enter a number.")


