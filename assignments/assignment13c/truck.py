# Author: Gatlin Lawson
class Truck:
    def __init__(self, x, y, height, color, extended_cab, xlong_bed):
        self.x = x
        self.y = y
        self.height = height
        self.color = color
        self.extended_cab = extended_cab
        self.xlong_bed = xlong_bed
    
    def draw(self, pen):    
        width=(self.height * 2)
        if self.xlong_bed:
            width += 50
        self.draw_truck_body(pen, width)
        
        #move to top of truck body
        pen.up()
        pen.setpos(xpos,ypos)
        pen.forward(width * .2)
        pen.setheading(90)
        pen.forward(self.height)
        pen.setheading(0)
        
        self.draw_cab(pen, width)
        if self.extended_cab:
            pen.forward(width * .15)
            self.draw_cab(pen, width)

    def draw_truck_body(self, pen, width):
        pen.up()
        pen.setpos(self.x,self.y)
        pen.down()
        pen.fillcolor(self.color)
        pen.begin_fill()
        for k in range(2):
            pen.forward(width)
            pen.left(90)
            pen.forward(self.height)
            pen.left(90)
        pen.end_fill()

        global ypos
        global xpos
        ypos=pen.ycor()
        xpos=pen.xcor()
        # tire 1
        pen.up()
        pen.forward(width * .2)
        pen.sety(ypos - 10)
        pen.down()
        pen.fillcolor("black")
        pen.begin_fill()
        pen.circle(self.height * .2)
        pen.end_fill()
        #tire 2
        pen.up()
        pen.forward(width * .6)
        pen.down()
        pen.fillcolor("black")
        pen.begin_fill()
        pen.circle(self.height * .2)
        pen.end_fill()

    def draw_cab(self, pen, width):
        #draw cab
        pen.down()
        pen.fillcolor(self.color)
        pen.begin_fill()
        for l in range(2):
            pen.forward(width *.2)
            pen.left(90)
            pen.forward(self.height *.4)
            pen.left(90)
        pen.up()
        pen.end_fill()
        
        #draw window
        pen.forward(width *.05)
        pen.down()
        pen.fillcolor("white")
        pen.begin_fill()
        for l in range(2):
            pen.forward(width *.1)
            pen.left(90)
            pen.forward(self.height *.2)
            pen.left(90)
        pen.up()
        pen.end_fill()


