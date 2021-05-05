# Author: Gatlin Lawson

from man import HangMan
import turtle
import random

screen = turtle.setup(575,575)
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()

draw = HangMan(0, 0, 50)

# Access word file
word_options = []
with open("assignments/finalproject/final_words.txt", "r") as file:
    for words in file:
        word_options.append(words)

def drawMan(player_guess):
    draw.drawHangMan(pen,player_guess)

def playHangMan():
    play_again = turtle.textinput("Hangman", "Would you like to play again? (Y)es or (N)o").lower().strip()

    if play_again == "y":
        pen.clear()
        pen.setheading(0)
        pen.setpos(0,0)
        get_letters()
    elif play_again == "n":
        exit()

def get_letters():
    negative = False
    while not negative:
        pen.color("black")
        pen.up()
        pen.setpos(-140, 160)
        word = random.choice(word_options).strip()
    
        for i in word:
            pen.write("_ ", True, font=("Courier", 16, "normal"))

        correct_guess = []
        guess_wrong = 0
        end = False
        while guess_wrong < 6 and not end:
            user_letter = turtle.textinput("Hangman", "Enter Letter")
            pen.up()
            pen.setpos(-140, 160)
            if user_letter not in correct_guess:
                for i in word:
                    if i == user_letter:
                        pen.write(user_letter + " ", True, font=("Courier", 16, "normal"))
                        correct_guess += user_letter
                    else:
                        pen.write("_ ", True, font=("Courier", 16, "normal"))
            else:
                print("You have used this letter")                
            
            if user_letter not in word:
                guess_wrong += 1
                drawMan(guess_wrong)
            if guess_wrong == 6:
                pen.up()
                pen.setpos(-140, 160)
                for i in word:
                    if i in correct_guess:
                        pen.write("_ ", True, font=("Courier", 16, "normal"))
                    else:
                        pen.write(i + " ", True, font=("Courier", 16, "normal"))
                pen.up()        
                pen.setpos(-100, -185)
                pen.down()
                pen.color("red")
                pen.write("Sorry, you lost", False, font=("Courier", 18, "normal"))
                pen.up()
                playHangMan()
            if len(correct_guess) == len(word):
                pen.up()
                pen.setpos(-100, -185)
                pen.down()
                pen.color("green")
                pen.write("YAY!!! You Won", False, font=("Courier,", 18, "normal"))
                pen.up()
                end = True
                playHangMan()
            
get_letters()

turtle.done()
