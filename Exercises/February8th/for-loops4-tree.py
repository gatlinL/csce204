# Author: Gatlin Lawson

import turtle

turtle.bgcolor("skyblue")
turtle.setup(500,500)
pen = turtle.Turtle()
pen.pensize(2)
pen.speed(.5)
pen.color("green")
pen.fillcolor("green")

treeHeight = 300
treeBottom = treeHeight/2
topTriangle = treeHeight * .2
middleTriangle = treeHeight * .3
bottomTriangle = treeHeight * .5

#top triangle
triangleSize = topTriangle
pen.up()
pen.setpos(-triangleSize/2, -treeHeight/2 + 120)
pen.down()

pen.begin_fill()
for i in range(3):
    pen.forward(triangleSize)
    pen.left(120)
pen.end_fill()

#middle triangle
triangleSize = middleTriangle
pen.up()
pen.setpos(-triangleSize/2, -treeHeight/2 + 70)
pen.down()

pen.begin_fill()
for i in range(3):
    pen.forward(triangleSize)
    pen.left(120)
pen.end_fill()

#bottom triangle
triangleSize = bottomTriangle
pen.up()
pen.setpos(-triangleSize/2,-treeHeight/2)
pen.down()

pen.begin_fill()
for i in range(3):
    pen.forward(triangleSize)
    pen.left(120)
pen.end_fill()

turtle.done()