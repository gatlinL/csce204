# Author: Gatlin Lawson

from truck import Truck
import turtle

turtle.setup(700,300)
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()

trucks = []
#x, y, height, color, extended_cab, xlong_bed
trucks.append(Truck(-250,45,50,"red",False, True))
trucks.append(Truck(-50,45,50,"green",True, False))
trucks.append(Truck(150,45,50,"pink",False, False))

def drawroad():
        # draw road
        pen.up()
        pen.setpos(-300,-100)
        pen.down()
        pen.fillcolor("grey")
        pen.begin_fill()
        for h in range(2):
            pen.forward(600)
            pen.left(90)
            pen.forward(200)
            pen.left(90)
        pen.end_fill()

        # draw road lines
        xcorr=-300
        for i in range(6):
            pen.up()
            pen.setpos(xcorr, 0)
            pen.down()
            pen.fillcolor("yellow")
            pen.begin_fill()
            for j in range(2):
                pen.forward(75)
                pen.left(90)
                pen.forward(15)
                pen.left(90)
            pen.end_fill()
            xcorr += 100

drawroad()

for truck in trucks:
    truck.draw(pen)

turtle.done()