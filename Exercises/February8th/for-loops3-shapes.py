# Author: Gatlin Lawson

import turtle

turtle.bgcolor("skyblue")
turtle.setup(500,500)
pen = turtle.Turtle()
pen.pensize(2)
pen.speed(.5)
pen.color("black")
pen.fillcolor("green")

squareSize = 200

pen.up()
pen.setpos(-squareSize/2,0)
pen.down()

#drawing a square
for i in range(4):
    pen.forward(squareSize)
    pen.left(90)

triangleSize = 100
pen.up()
pen.setpos(-triangleSize/2,0)
pen.down()

#drawing a triangle
pen.begin_fill()
for i in range(3):
    pen.forward(triangleSize)
    pen.left(120)
pen.end_fill()


turtle.done()