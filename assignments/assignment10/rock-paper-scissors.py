# Author: Gatlin Lawson

import random

print("Welcome to Rock Paper Scissors")

# track wins a losses
win = 0
loss = 0
tie = 0

while True:
    answer = input("(P)lay or (Q)uit: ").lower()

    if answer == "q":
        break

    elif answer == "p":
        userMove = input("Enter (R)ock, (P)aper, or (S)cissors: ").lower()
        randomNumber = random.randint(1,3)
        
        # computer move
        if randomNumber == 1:
            computerMove = "r"
            print("Computer choose: r")
        elif randomNumber == 2:
            computerMove = "p"
            print("Computer choose: p")
        elif randomNumber == 3:
            computerMove = "s"
            print("Computer choose: s")
        
        #win or lose
        if userMove == computerMove:
            print("Tie!")
            tie += 1
        elif userMove == "r" and computerMove == "s":
            print("You Won!")
            win += 1
        elif userMove == "s" and computerMove == "p":
            print("You Won!")
            win += 1
        elif userMove == "p" and computerMove == "r":
            print("You won!")
            win += 1
        elif userMove == "r" and computerMove == "p":
            print("Computer Won!")
            loss += 1
        elif userMove == "p" and computerMove == "s":
            print("Computer Won!")
            loss += 1
        elif userMove == "s" and computerMove == "r":
            print("Computer Won!")
            loss += 1
    else:
        print("Invalid Command")

print(f"You won {win} rounds")
print(f"The computer won {loss} rounds")
print(f"You tied {tie} rounds")