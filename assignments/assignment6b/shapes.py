# Author: Gatlin Lawson

import turtle

turtle.setup(575,575)
pen = turtle.Turtle()
pen.speed(1)
pen.pensize(5)
pen.hideturtle()

shape = ["circle", "square", "triangle", "star"]
shapeArray = []
xPosition = -150

numberShapes = turtle.numinput("Number of Shapes", "How many shapes would you like to draw?")

shapeSize = 200/numberShapes

for num in range(int(numberShapes)):    
    shapeInput = turtle.textinput("Shapes", "Enter shape (circle, square, triangle, or star):").lower().strip()
    shapeArray.append(shapeInput)

pen.up()
pen.setpos(xPosition,0)
for shape in shapeArray:
    pen.down()
    if shape == "circle":
        pen.up()
        pen.forward(shapeSize/2)
        pen.down()
        pen.circle(shapeSize/2)
        pen.up()
        pen.backward(shapeSize/2)
        pen.down()
    elif shape == "square":
        for i in range(4):
            pen.forward(shapeSize)
            pen.left(90)
    elif shape == "triangle":
        for i in range(3):
            pen.forward(shapeSize)
            pen.left(120)
    elif shape == "star":
        pen.up()
        pen.sety(shapeSize/1.75)
        pen.down()
        for i in range(5):
            pen.forward(shapeSize)
            pen.right(144)
        pen.up()
        pen.sety(-shapeSize/1.75)
        pen.down()
    else:
        pen.write("x",font=('Arial',16,'normal'))
    pen.up()
    pen.forward(shapeSize * 2)

turtle.done()