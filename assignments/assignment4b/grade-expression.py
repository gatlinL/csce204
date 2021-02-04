# Author: Gatlin Lawson

import turtle

turtle.setup(500,500)
pen = turtle.Turtle()
pen.pensize(2)
pen.speed(.5)
pen.color("black")
pen.fillcolor("white")

grade = turtle.textinput("Grade", "Enter Grade:")

faceRadius=100

#Smiley Face
if grade >= "80":
    #Face
    pen.up()
    pen.setpos(0,0)
    pen.down()
    pen.setheading(0)
    pen.circle(faceRadius)
    #Left Eye
    pen.up()
    pen.setpos(-faceRadius * .5 + 10 , faceRadius)
    pen.down()
    pen.fillcolor("black")
    pen.begin_fill()
    pen.circle(faceRadius/2 * .3)
    pen.end_fill()
    #Right Eye
    pen.up()
    pen.setpos(faceRadius * .5 - 10 , faceRadius)
    pen.down()
    pen.fillcolor("black")
    pen.begin_fill()
    pen.circle(faceRadius/2 * .3)
    pen.end_fill()
    #Smile
    pen.up()
    pen.setpos(-faceRadius/2 + 10,faceRadius/2 + 10)
    pen.down()
    pen.setheading(-60)
    pen.circle(faceRadius/2, 120)
#Flat Smile
elif grade >= "70":
    #Face
    pen.up()
    pen.setpos(0,0)
    pen.down()
    pen.setheading(0)
    pen.circle(faceRadius)
    #Left Eye
    pen.up()
    pen.setpos(-faceRadius * .5 + 10 , faceRadius)
    pen.down()
    pen.fillcolor("black")
    pen.begin_fill()
    pen.circle(faceRadius/2 * .3)
    pen.end_fill()
    #Right Eye
    pen.up()
    pen.setpos(faceRadius * .5 - 10 , faceRadius)
    pen.down()
    pen.fillcolor("black")
    pen.begin_fill()
    pen.circle(faceRadius/2 * .3)
    pen.end_fill()
    #Smile
    pen.up()
    pen.setpos(-faceRadius/2 + 10,faceRadius/2 + 10)
    pen.down()
    pen.setheading(0)
    pen.forward(faceRadius)
#Sad Face
else:
    #Face
    pen.up()
    pen.setpos(0,0)
    pen.down()
    pen.setheading(0)
    pen.circle(faceRadius)
    #Left Eye
    pen.up()
    pen.setpos(-faceRadius * .5 + 10 , faceRadius)
    pen.down()
    pen.fillcolor("black")
    pen.begin_fill()
    pen.circle(faceRadius/2 * .3)
    pen.end_fill()
    #Right Eye
    pen.up()
    pen.setpos(faceRadius * .5 - 10 , faceRadius)
    pen.down()
    pen.fillcolor("black")
    pen.begin_fill()
    pen.circle(faceRadius/2 * .3)
    pen.end_fill()
    #Frown
    pen.up()
    pen.setpos(faceRadius/2 * .85 ,faceRadius/2 + 10)
    pen.down()
    pen.setheading(120)
    pen.circle(faceRadius/2, 120)

pen.up()
pen.goto(-50,-50)

turtle.done()