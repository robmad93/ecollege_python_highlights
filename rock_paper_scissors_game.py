# Code to build a rock-paper-scissor game using Python, where the player competes against the computer.

import random
import sys
from enum import Enum


# Define an enumeration for Rock, Paper, and Scissors
class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


# Print an empty line for better readability
print("")

# Prompt the player to enter their choice
playerchoice = input("Enter... \n1 for Rock, \n2 for Paper,or \n3 for Scissors:\n\n")

# Convert the player's choice to an integer
player = int(playerchoice)

# Check if the player's choice is valid (1, 2, or 3)
if player < 1 | player > 3:
    sys.exit("You must enter 1, 2, or 3.")

# Generate the computer's choice randomly from the set {1, 2, 3}
computerchoice = random.choice("123")
computer = int(computerchoice)

# Print the player's and computer's choices
print("")
print("You chose " + str(RPS(player)).replace("RPS.", "") + ".")
print("Python chose " + str(RPS(computer)).replace("RPS.", "") + ".")
print("")

# Determine and print the game outcome based on the player's and computer's choices
if player == 1 and computer == 3:
    print("🎉 You win!")
elif player == 2 and computer == 1:
    print("🎉 You win!")
elif player == 3 and computer == 2:
    print("🎉 You win!")
elif player == computer:
    print("😲 Tie game!")
else:
    print("🐍 Python wins!")
