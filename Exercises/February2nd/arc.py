# Author: Gatlin Lawson

import turtle

turtle.setup(575,575)
pen = turtle.Turtle()
pen.speed(.5)
pen.pensize(2)
pen.hideturtle()

pen.up()
pen.setpos(-turtle.window_width()/2,0)
pen.down()
pen.forward(turtle.window_width())
pen.up()
pen.setpos(0,-turtle.window_height()/2)
pen.down()
pen.setheading(90)
pen.forward(turtle.window_height())

arcRadius = 100

#pen.up()
#pen.setpos(-arcRadius,0)
#pen.down()
#pen.setheading(-60)
#pen.circle(arcRadius, 120)

pen.up()
pen.setpos(arcRadius, -arcRadius)
pen.down()
pen.setheading(120)
pen.circle(arcRadius, 120)



turtle.done()