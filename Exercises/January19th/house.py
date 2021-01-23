# Author: Gatlin Lawson

import turtle

turtle.bgcolor("grey")
turtle.setup(500,500)
pen = turtle.Turtle()
pen.pensize(2)
pen.speed(.5)

# draw house

# draw body of house
pen.penup()
pen.setpos(-100,-150)
pen.pendown()
pen.fillcolor("red")
pen.begin_fill()
pen.forward(200)
pen.left(90)
pen.forward(200)
pen.left(90)
pen.forward(200)
pen.left(90)
pen.forward(200)
pen.end_fill()

# draw roof
pen.penup()
pen.setheading(90)
pen.forward(200)
pen.pendown()
pen.fillcolor("black")
pen.begin_fill()
pen.setheading(0)
pen.forward(200)
pen.left(120)
pen.forward(200)
pen.left(120)
pen.forward(200)
pen.end_fill()

# draw door
pen.penup()
pen.setheading(-90)
pen.forward(200)
pen.setheading(0)
pen.forward(75)
pen.pendown()
pen.fillcolor("blue")
pen.begin_fill()
pen.forward(50)
pen.left(90)
pen.forward(100)
pen.left(90)
pen.forward(50)
pen.left(90)
pen.forward(100)
pen.end_fill()

# draw doorknob
pen.penup()
pen.setheading(0)
pen.forward(40)
pen.setheading(90)
pen.forward(60)
pen.fillcolor("black")
pen.begin_fill()
pen.circle(5)
pen.end_fill()






turtle.done()