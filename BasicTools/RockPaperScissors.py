# Simple rock, paper, scissor generator

import random

options = ("rock", "paper", "scissors")
running = True                      # refactor variable names all at once by refactoring

while running:                      # running a while loop while the boolean variable is true is better for longer code that can make it hard to find a break statement

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    else:
        print("You lose!")

    if not input("Play again? (y/n): ").lower == "y":
        running = False   
                                          
print("Thanks for playing!")
