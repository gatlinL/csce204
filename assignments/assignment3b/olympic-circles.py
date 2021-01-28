# Author: Gatlin Lawson

# Question to user
input("How large on a scale of 1 to 10 would you like to draw your Olympic Rings: ")


import turtle

turtle.bgcolor("white")

pen = turtle.Turtle()

pen.speed(0)
pen.pensize(8)

# Black Ring
pen.pencolor("black")
pen.circle(80)

# Blue Ring
pen.penup()
pen.goto(-200,0)
pen.pendown()
pen.pencolor("blue")
pen.circle(80)

# Red Ring
pen.penup()
pen.goto(200,0)
pen.pendown()
pen.pencolor("red")
pen.circle(80)

# Yellow Ring
pen.penup()
pen.goto(-100,-100)
pen.pendown()
pen.pencolor("yellow")
pen.circle(80)

# Green Ring
pen.penup()
pen.goto(100,-100)
pen.pendown()
pen.pencolor("green")
pen.circle(80)

turtle.done()