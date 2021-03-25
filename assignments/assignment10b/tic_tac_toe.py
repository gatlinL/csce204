# Author: Gatlin Lawson

import turtle

turtle.setup(575,575)
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()

gridSize = 300

isX = True

def draw_grid():
    pen.up()
    pen.goto(-150, -150)
    pen.pendown()
    pen.left(90)
    for i in range(2):
        for j in range(4):
            pen.right(90)
            pen.pendown()
            pen.forward(gridSize)
            pen.right(180)
            pen.forward(gridSize)
            pen.right(90)
            pen.up()
            pen.forward(gridSize/3)
        pen.backward(gridSize/3)
        pen.right(90)

def draw_x(x,y):
    xSize = gridSize * .1
    xSize1 = xSize * 2

    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.right(45)
    pen.forward(xSize)
    pen.backward(xSize1)
    pen.forward(xSize)
    pen.left(90)
    pen.forward(xSize)
    pen.backward(xSize1)
    pen.right(45)

def draw_O(x,y):
    circleSize = gridSize *.1
    pen.up()
    pen.setpos(x - circleSize, y)
    pen.down()
    pen.circle(circleSize)

def draw_x_or_O(x,y):
    global isX

    if isX:
        draw_x(x,y)
        isX = False
    else:
        draw_O(x,y)
        isX = True   


def getXCoord(x):
    #get x centered location
    global newx

    if x <= -51 and x >= -150:
        #column1
        newx=-100
    elif x <= 50 and x > -50:
        #column2
        newx=0
    elif x <= 150 and x > 51:
        #column3
        newx=100

def getYCoord(y):
    #get y centered location
    global newy
    
    if y <= -51 and y >= -150:
        #column1
        newy=-100
    elif y <= 50 and y > -50:
        #column2
        newy=0
    elif y <= 150 and y > 51:
        #column3
        newy=100
       

def drawPlay(x,y):
    #print("You clicked at this coordinate({0},{1})".format(x,y))
    #Stay on gameboard
    if (-150 <= x <= 150) and (-150 <= y <= 150):
        getXCoord(x)
        getYCoord(y)
        draw_x_or_O(newx,newy)


#START HERE    
draw_grid()
turtle.onscreenclick(drawPlay)


turtle.done()
