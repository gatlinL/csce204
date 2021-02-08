# Author: Gatlin Lawson

import random

print("Welcome to our multiplication Game")
command = input("Would you like to play, (Y)es or (N)o: ").lower().strip()

x = random.randint(1,10)
y = random.randint(1,10)

while command == "y":
    answer = int(input(str(x) + "x" + str(y) + ":"))

    if answer == x*y:
        print(f"{x*y} is correct, congrats!")
    else:
        print(f"{answer} is incorrect")
    command = input("Would you like to try again (Y)es or (N)o: ")

if command == "n":
    print("Thanks for playing!")