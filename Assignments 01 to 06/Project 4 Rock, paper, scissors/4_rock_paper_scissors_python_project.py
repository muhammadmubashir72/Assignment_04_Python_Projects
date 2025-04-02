# Rock, paper, scissors Python Project
# In this Kylie Ying tutorial, you will work with random.choice(),
#  if statements, and getting user input. This is a great project to 
# help you build on the fundamentals like conditionals and functions.
import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    if (user_choice == "rock" and computer_choice == "scissors") or \
       (user_choice == "scissors" and computer_choice == "paper") or \
       (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    return "computer"

def play_game():
    print("Welcome to Rock, Paper, Scissors - Best of 3! 🏆")
    
    user_score, computer_score = 0, 0
    for _ in range(3):
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice, try again!")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        winner = get_winner(user_choice, computer_choice)
        if winner == "user":
            print("🎉 You win this round!")
            user_score += 1
        elif winner == "computer":
            print("💻 Computer wins this round!")
            computer_score += 1
        else:
            print("It's a tie! 🤝")

    if user_score > computer_score:
        print("🏆 You won the game!")
    elif computer_score > user_score:
        print("😢 Computer wins the game!")
    else:
        print("Game ended in a tie!")

if __name__ == "__main__":
    play_game()
