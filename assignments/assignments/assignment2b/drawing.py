# Author: Gatlin Lawson

import turtle 

turtle.bgcolor("grey")

pen = turtle.Turtle()

pen.pensize(0)
pen.speed(0)

#draw circle (head)
pen.fillcolor("orange")
pen.begin_fill()
pen.circle(100)
pen.end_fill()

#draw eyes (circles)
pen.penup()
pen.goto(-40,100)
pen.pendown()

pen.fillcolor("black")
pen.begin_fill()
pen.circle(20)
pen.end_fill()

pen.penup()
pen.goto(40,100)
pen.pendown()

pen.fillcolor("black")
pen.begin_fill()
pen.circle(20)
pen.end_fill()

#draw nose (triangle)
pen.pensize(5)
pen.penup()
pen.goto(0,65)
pen.setheading(110)
pen.pendown()
pen.color("black")
pen.begin_fill()
pen.forward(20)
pen.setheading(0)
pen.forward(10)
pen.setheading(-110)
pen.forward(20)
pen.end_fill()
starting_nose_x = pen.xcor()
starting_nose_y = pen.ycor()

#draw mouth (half circle)
pen.left(120)
pen.forward(10)
pen.right(16)
pen.forward(17)

pen.penup()
pen.goto(starting_nose_x,starting_nose_y)
pen.pendown()
pen.setheading(-180)

pen.forward(10)
pen.left(16)
pen.forward(10)

# draw ears
pen.penup()
pen.goto(-55,185)
pen.setheading(-290)
pen.pendown()

pen.color("orange")
pen.begin_fill()
pen.forward(35)
pen.setheading(-50)
pen.forward(30)
pen.end_fill()

pen.penup()
pen.goto(55,185)
pen.setheading(-245)
pen.pendown()
pen.begin_fill()
pen.forward(35)
pen.setheading(-120)
pen.forward(30)
pen.end_fill()

# body (circle)
pen.penup()
pen.goto(-125,-50)
pen.pendown()

pen.pensize(0)
pen.fillcolor("orange")
pen.begin_fill()
pen.circle(150)
pen.end_fill()

# arms 
pen.penup()
pen.goto(-135,-70)
pen.setheading(-200)
pen.pendown()

pen.fillcolor("orange")
pen.begin_fill()
pen.forward(90)
pen.setheading(-110)
pen.forward(40)
pen.setheading(-20)
pen.forward(100)
pen.end_fill()

pen.penup()
pen.goto(145,-70)
pen.setheading(20)
pen.pendown()

pen.fillcolor("orange")
pen.begin_fill()
pen.forward(90)
pen.setheading(-70)
pen.forward(40)
pen.setheading(-160)
pen.forward(100)
pen.end_fill()

#legs
pen.pensize(5)
pen.penup()
pen.goto(-50,-225)
pen.down()
pen.color("black")
pen.fillcolor("orange")
pen.begin_fill()
pen.circle(50)
pen.end_fill()

pen.penup()
pen.goto(50,-225)
pen.down()
pen.color("black")
pen.fillcolor("orange")
pen.begin_fill()
pen.circle(50)
pen.end_fill()

turtle.done()