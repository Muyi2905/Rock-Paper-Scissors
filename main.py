import random

def game():
    choices = ["rock", "paper", "scissors"]
    user_choice = ""
    
while user_choice not in choices:
        user_choice = input("Enter your choice between 'rock', 'paper', and 'scissors': ").lower()