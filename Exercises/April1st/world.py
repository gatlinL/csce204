# Author: Gatlin Lawson

import turtle
import random

turtle.setup(575,575)
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()

def getScene():
    sceneColors = []
    with open("Exercises/April1st/scene.txt") as file:
        for line in file:
            sceneColor = line.replace("\n", "").strip().lower()
            sceneColors.append(sceneColor)
        return sceneColors

def drawColorStrip(y, height, color):
    pen.up()
    pen.setpos(-turtle.window_width()/2, y)
    pen.down()
    pen.fillcolor(color)
    pen.begin_fill()
    for i in range(4):
        if i % 2 == 0:
            pen.forward(turtle.window_width())
        else:
            pen.forward(height)
        pen.left(90)
    pen.end_fill()

colorList = getScene()
numColors = len(colorList)
height = turtle.window_height()/numColors
y = turtle.window_height()/2

for myColor in colorList:
    y -= height
    drawColorStrip(y, height, myColor)

turtle.done()