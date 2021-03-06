# Author: Gatlin Lawson

import turtle
import random

turtle.setup(575,575)
pen = turtle.Turtle()
pen.speed(.4)
pen.pensize(2)
pen.hideturtle()

gridHeight = int(turtle.numinput("Pyramid", "Enter Height: ", 5, 1, 10))
widthPadding = turtle.window_width()/gridHeight
padding = widthPadding * .5

shapeNo=gridHeight

#GET COLORS
colors = []
for j in range(gridHeight):
    rowColor =(turtle.textinput("Pyramid", "Enter color of row " + str(j+1) +":"))
    #enter color into array
    colors.append(rowColor)

#LOOP THROUGH ROWS

for row in range(gridHeight):
    x = - turtle.window_width()/2 + widthPadding - (shapeNo * padding)
    y = - turtle.window_height()/2 + padding + row * widthPadding

    fcolor = colors[row]
    
    for col in range(shapeNo):
        pen.up()
        pen.setpos(x/2,y/2.25)
        pen.down()

        #build triangle
        pen.fillcolor(fcolor)
        pen.begin_fill()
        for i in range(0,3):
            pen.left(120)
            pen.forward(padding)
        pen.end_fill()
        x += widthPadding
    shapeNo -= 1    
            
turtle.done()
