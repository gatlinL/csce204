# Author: Gatlin Lawson

import turtle
import random

turtle.bgcolor("skyblue")
turtle.setup(500,500)
pen = turtle.Turtle()
pen.pensize(2)
pen.speed(.5)
pen.color("black")
style = ("Arial", 12, "normal")
pen.hideturtle()
turtle.hideturtle()
turtle.speed(0)
turtle.colormode(255)

numNames = int(turtle.numinput("Names", "Number of names", 10, 0, 100))

for i in range(numNames):
    r = random.randrange(0, 256)
    g = random.randrange(0, 256)
    b = random.randrange(0, 256)
    turtle.color(r,g,b)

    x = random.randint(-turtle.window_width()/2, turtle.window_width()/2)
    y = random.randint(-turtle.window_height()/2, turtle.window_height()/2)
    turtle.penup()
    turtle.setpos(x,y)
    turtle.down()
    turtle.write("Gatlin", font=style)

turtle.done()
