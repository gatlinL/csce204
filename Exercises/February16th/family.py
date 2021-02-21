# Author: Gatlin Lawson

import turtle
import random

turtle.setup(575,575)
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()

colors = ("violet", "indigo", "blue", "green", "yellow", "orange", "red")
family = []

while True:
    response = turtle.textinput("Family", "Enter family members name")
    if response is None: break
    family.append(response)

if len(family) > 0:
    for i in range (100):
        pen.color(colors[i%len(colors)])
        pen.up()
        pen.forward(i * 4)
        pen.down()
        style = ("Arial", int((i+4)/4), "bold")
        pen.write(family[i%len(family)], font = style)
        pen.left(360/len(family) + 2)


turtle.done()