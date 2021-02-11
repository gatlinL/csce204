# Author: Gatlin Lawson

import turtle

turtle.bgcolor("skyblue")
turtle.setup(500,500)
pen = turtle.Turtle()
pen.pensize(2)
pen.speed(.5)
pen.color("black")

houseSize = 100

#Square House
pen.up()
pen.setpos(-houseSize/2,-100)
pen.down()

pen.setheading(0)
pen.fillcolor("orange")
pen.begin_fill()
for i in range(4):
    pen.forward(houseSize)
    pen.right(90)
pen.end_fill()

#Triangle House Roof

pen.fillcolor("purple")
pen.begin_fill()
pen.left(60)
for i in range(3):
    pen.forward(houseSize)
    pen.right(120)
    pen.forward(20)
pen.end_fill()

#Tree
pen.up()
pen.setpos(houseSize/2 + 30,-houseSize - 100)
pen.down()

pen.setheading(0)
pen.color("brown")
pen.fillcolor("brown")
pen.begin_fill()
for i in range(4):
    pen.forward(houseSize/2 - 10)
    pen.left(90)
pen.end_fill()

pen.forward(houseSize/5)
pen.left(90)
pen.forward(houseSize/4)
pen.setheading(0)
pen.color("green")

pen.fillcolor("green")
pen.begin_fill()
pen.circle(houseSize*.3)
pen.end_fill()

#Sun
def drawRays(t, length, radius):
    for i in range(4):
        t.up()
        t.forward(radius)
        t.down()
        t.forward(length)
        t.up()
        t.backward(length + radius)
        t.left(30)

pen.up()
pen.goto(-houseSize,houseSize/1.2)
pen.down()

pen.color("yellow")
pen.fillcolor("yellow")
pen.begin_fill()
pen.circle(houseSize/6)
pen.end_fill()

pen.up()
pen.goto(-houseSize, houseSize)
pen.down()
drawRays(pen, houseSize/2, houseSize/5)
pen.right(360)
drawRays(pen, houseSize/2, houseSize/5)
pen.left(360)
drawRays(pen, houseSize/2, houseSize/5)


turtle.done()