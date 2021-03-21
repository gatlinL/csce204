# Author: Gatlin Lawson

import turtle
import random

turtle.setup(575,575)
#maximize screen
#turtle.screensize()
#turtle.setup(width = 1.0, height = 1.0)

winwidth=turtle.window_width()
winheight=turtle.window_height()

pen = turtle.Turtle()
pen.speed(.2)
pen.pensize(2)
pen.hideturtle()

baseColor="black"
Colors = (["Blue","Orange","Green","Yellow","Red","White"])

def draw_square(x, y, width, color):
    pen.up()
    pen.setpos(x,y)
    pen.down()
    
    pen.fillcolor(color)

    pen.begin_fill()
    for i in range(4):
        pen.forward(width)
        pen.left(90)
    pen.end_fill()


def draw_rubics_cube(x, y, width):
    draw_square(x, y, width, baseColor)
    widthPadding = width/3
    squarePadding = widthPadding * 1.25

    #1st row
    for i in range(3):
        fcolor = random.choice(Colors)
        draw_square(x, y , widthPadding ,fcolor)
        x += widthPadding

    #back to new row
    x=stx
    y=(sty + widthPadding)
    newy=y

    #2nd row
    for i in range(3):
        fcolor = random.choice(Colors)
        draw_square(x, y , widthPadding ,fcolor)
        x += widthPadding

    #back to new row
    x=stx
    y=(newy + widthPadding)

    #3rd row
    for i in range(3):
        fcolor = random.choice(Colors)
        draw_square(x, y , widthPadding ,fcolor)
        x += widthPadding
        
#Draws 10 rubics cubes        
for i in range(10):
    x = random.randint(-int(winwidth/2), int(winwidth/2))
    y = random.randint(-int(winheight/2), int(winheight/2))

    #moving it from edge
    if (x < 0):
        x += 75
    elif (x > 0):
        x -= 75
    else:
        x
    
    if (y < 0):
        y += 75
    elif (y > 0):
        y -= 75
    else:
        y

    #starting coordinates
    stx=x
    sty=y
    
    size = random.randint(20, 100)

    draw_rubics_cube(x,y,size)


turtle.done()
