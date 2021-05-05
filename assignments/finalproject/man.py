# Author: Gatlin Lawson
class HangMan:
    def __init__(self, x, y, width):
        self.x = x
        self.y = y
        self.width = width

    def drawHangMan(self, pen, player_guess):    
        # draw head
        if player_guess == 1:
            pen.up()
            pen.setpos(self.x ,self.y)
            pen.down()
            pen.circle(self.width)
        # draw body
        elif player_guess == 2:
            pen.up()
            pen.setpos(self.x,self.y)
            pen.down()
            pen.setheading(270)
            pen.forward(self.width * 2)
        # draw left arm
        elif player_guess == 3:
            pen.up()
            pen.setpos(self.x ,self.y - self.width)
            pen.down()
            pen.setheading(135)
            pen.forward(self.width)
        # draw right arm
        elif player_guess == 4:
            pen.up()
            pen.setpos(self.x, self.y - self.width)
            pen.down()
            pen.setheading(45)
            pen.forward(self.width)
        # draw left leg
        elif player_guess == 5:
            pen.up()
            pen.setpos(self.x, self.y - (self.width * 2))
            pen.down()
            pen.setheading(225)
            pen.forward(self.width)
        # draw right leg
        elif player_guess == 6:
            pen.up()
            pen.setpos(self.x, self.y - (self.width * 2))
            pen.down()
            pen.setheading(315)
            pen.forward(self.width)
