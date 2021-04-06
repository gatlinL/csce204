# Author: Gatlin Lawson

import turtle
import os

turtle.setup(800,600)

pen = turtle.Turtle()
pen.speed(.2)
pen.pensize(2)
pen.hideturtle()


from os.path import abspath, dirname
CURR_DIR = dirname(abspath(__file__))
FILE_NAME_SCENE = "scene.txt"
FILE_NAME_SCENE = os.path.join(CURR_DIR, FILE_NAME_SCENE)

treecolor="darkgreen"
starcolor="yellow"


#access file
def getScene():
    scenePictures = []
    with open(FILE_NAME_SCENE, "r") as file:
        for line in file:
            scenePicture = line.replace("\n", "").strip().lower()
            scenePictures.append(scenePicture)
        return scenePictures

# draw Triangle function
def drawTriangle(x, y, size):
    pen.up()
    pen.setpos(x,y)
    pen.down()
    for i in range(3):
        pen.forward(size)
        pen.left(120)
        
# draw upside-down triangle
def drawUpsideDownTriangle(x, y, size):
    pen.up()
    pen.setpos(x,y)
    pen.down()
    for i in range(3):
        pen.forward(size)
        pen.left(-120)
        
# draw Star
def drawStar(x, width):
    pen.color(starcolor)
    pen.fillcolor(starcolor)
    newy = (y + SheightPadding)

    pen.begin_fill()
    drawTriangle(x, y, width)
    pen.end_fill()

    pen.begin_fill()
    drawUpsideDownTriangle(x, newy, width)
    pen.end_fill()
    
# draw Tree
def drawTree(x, width):
    pen.color(treecolor)
    pen.fillcolor(treecolor)
    newy = (y - TheightPadding)
    newx = x
    newwidth=width
    
    for i in range(3):
        pen.begin_fill()
        drawTriangle(newx, newy, newwidth)
        newy += TheightPadding
        newwidth -= (newwidth/6)
        newx += (newwidth/6) - 4
        pen.end_fill()
    

#START HERE
scenePictures=getScene()
numPictures=len(scenePictures)

width = (turtle.window_width()/numPictures) - 50
TheightPadding = width/3
SheightPadding = width/2
widthPadding = width * 1.25

x = -300
y = 0

    
for num in range(numPictures):
    pic=scenePictures[num]

    if pic == "star":
        drawStar(x, width)
    elif pic == "tree":
        drawTree(x, width)
    else:
        pen.write("X")
    x += widthPadding

turtle.done()
