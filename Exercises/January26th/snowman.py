# Author: Gatlin Lawson

import turtle

turtle.bgcolor("skyblue")
turtle.setup(500,500)
pen = turtle.Turtle()
pen.pensize(2)
pen.speed(.5)
pen.color("black")
pen.fillcolor("white")

largeCircle = 75
mediumCircle = largeCircle * 3/4
smallCircle = mediumCircle * 3/4
eyeSize = smallCircle * 0.1
noseSize = smallCircle * 0.2

# large circle
pen.sety(-largeCircle)
pen.begin_fill()
pen.circle(largeCircle)
pen.end_fill()

# medium circle
pen.up()
pen.sety(.5 * largeCircle)
pen.down()
pen.begin_fill()
pen.circle(mediumCircle)
pen.end_fill()

# small circle
pen.up()
pen.sety(.5 * largeCircle + 1.5 * mediumCircle)
pen.down()
pen.begin_fill()
pen.circle(smallCircle)
pen.end_fill()

# left eye
pen.fillcolor("black")
pen.up()
pen.sety(.5 * largeCircle + 1.5 * mediumCircle + smallCircle)
pen.setx(-smallCircle * .3)
pen.down()
pen.begin_fill()
pen.circle(eyeSize)
pen.end_fill()

# right eye
pen.fillcolor("black")
pen.up()
pen.sety(.5 * largeCircle + 1.5 * mediumCircle + smallCircle)
pen.setx(smallCircle * .3)
pen.down()
pen.begin_fill()
pen.circle(eyeSize)
pen.end_fill()

# nose
pen.fillcolor("orange")
pen.up()
pen.sety(.5 * largeCircle + 1.5 * mediumCircle + smallCircle * .7)
pen.setx(-noseSize * .5)
pen.down
pen.begin_fill()

pen.setheading(0)
pen.color("orange")
pen.forward(noseSize)
pen.left(120)
pen.forward(noseSize)
pen.left(120)
pen.forward(noseSize)

pen.up()
pen.setpos(-100, -100)

pen.end_fill()

turtle.done()