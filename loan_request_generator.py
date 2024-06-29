"""This code reads loan requests from a text file and processes them based on available funds ("kitty").
It performs two main operations: initially, it checks and prints the status of the loan requests, 
and then it writes the results to the same text file."""

import os

os.getcwd()  # Check to ensure working directory is correct.

text = "INITIAL BUILD"
title = text.center(70, "=")
print(title)

# First, I'll focus on retrieving the elements and setting up the for loop construct
# before I attempt to make changes to the file. This represents my initial build.


requests = []
kitty = 500


with open(
    "loan_requests.txt"
) as file:  # "with" ensures file is closed upon completion.
    requests = [
        line.rstrip() for line in file
    ]  # Remove whitespace characters and fill empty requests list.
print(
    requests
)  # Requests list now contains request values. Still need to convert into integers.

requests = [int(line) for line in requests]  # Convert strings to integers.

for line in requests:
    if line <= kitty:
        print("{} - Paid!".format(line))
        kitty = kitty - line
    elif line > kitty:
        if kitty != 0:
            print(
                "{} request cannot be processed in full (Insufficient funds available). Amount paid: {}".format(
                    line, kitty
                )
            )
            kitty = 0  # Crucial line: prevents kitty going into negative values
        else:
            print("Request of {} is UNPAID!".format(line))

# Implement changes to the file.
text2 = "FINAL BUILD"
title2 = text2.center(70, "=")
print(title2)


# Reseting the "kitty" variable.

kitty = 500
# For loop, adding changes to the text file.
with open("loan_requests.txt", "a") as file:
    for line in requests:
        if line <= kitty:
            print("{} - Paid!".format(line))
            kitty = kitty - line
            file.write("\nRequest of {} paid in full.".format(line))
        elif line > kitty:
            if kitty != 0:
                print(
                    "{} request cannot be processed in full (Insufficient funds available). Amount paid: {}".format(
                        line, kitty
                    )
                )
                file.write(
                    "\nRequest of {} could not be paid in full. Partial payment of {} made.".format(
                        line, kitty
                    )
                )
                kitty = 0
            else:
                print("Request of {} is UNPAID!".format(line))
                file.write("\nOutstanding Request:{}".format(line))
