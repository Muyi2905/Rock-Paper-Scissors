import random

def game():
    choices = ["rock", "paper", "scissors"]
    user_choice = ""
    
while user_choice not in choices:
        user_choice = input("Enter your choice between 'rock', 'paper', and 'scissors': ").lower()
print("You:", user_choice)

computer_choice = random.choice(choices)
print("Computer:", computer_choice)

if user_choice == computer_choice:
        print("It's a tie!")
elif user_choice == "rock":
        if computer_choice == "paper":
            print("You lose!")
        else:
            print("You win!")
    
elif user_choice == "paper":
        if computer_choice == "scissors":
            print("You lose!")
        else:
            print("You win!")
elif user_choice == "scissors":
        if computer_choice == "rock":
            print("You lose!")
        else:
            print("You win!")
