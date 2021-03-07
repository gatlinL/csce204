# Author: Gatlin Lawson

import turtle

#turtle.setup(800,600)

#maximize screen
turtle.screensize()
turtle.setup(width = 1.0, height = 1.0)

winwidth=turtle.window_width()
winheight=turtle.window_height()

pen = turtle.Turtle()
pen.speed(.2)
pen.pensize(2)
pen.hideturtle()

style = ("Arial", 12)

firstNames = []
lastNames = []
genders = []
phoneNumbers = []

# HEAD
def draw_head():
  pen.circle(25)
  pen.setheading(270)

# TORSO
def draw_torso():
  pen.forward(100)
  pen.penup()
  pen.backward(75)
  pen.penup()

# BOTH ARMS
def draw_arms():
  pen.setheading(180)
  pen.forward(50)
  pen.down()
  pen.setheading(0)
  pen.forward(100)
  pen.penup()
  pen.backward(50)
  pen.setheading(270)
  pen.forward(75)

# LEFT LEG
def draw_left_leg():
  pen.pendown()
  pen.setheading(225)
  pen.forward(75)
  pen.penup()
  pen.backward(75)
  
# RIGHT LEG
def draw_right_leg():
  pen.pendown()
  pen.setheading(315)
  pen.forward(75)
  pen.penup()

# DRAW STICK FIGURE
def draw_stick_figure():
  draw_head()
  draw_torso()
  draw_arms()
  draw_left_leg()
  draw_right_leg()

# MAN
def draw_man():
  #set color to blue
  pen.color("blue")
  draw_stick_figure()
  pen.up()
  pen.setheading(0)

# WOMAN
def draw_woman():
  #set color to pink
  pen.color("pink")
  draw_stick_figure()
  #draw skirt line for woman
  pen.pendown()
  pen.setheading(180)
  pen.forward(105)
  pen.up()
  pen.setheading(0)

#STARTS HERE
numberContacts = turtle.numinput("Contacts", "How many contacts do you have?")

#GETTING TURTLE LOCATION READY
ypos=pen.ycor()
xpos=pen.xcor()

pen.up()
xpos-=(winwidth/2)
xpos+=50
ypos+=(winheight/2)
ypos-=50
pen.setpos(xpos,ypos)

#TITLE
pen.down()
pen.write("My Contact List",font=('Arial', 20, 'bold'))
pen.up()

ypos-=50
pen.setpos(xpos,ypos)

#GET CONTACT INFO
for num in range(int(numberContacts)):
# taking four inputs at a time
    w, x, y, z = turtle.textinput("Contact", "Enter First Name, Last Name, Gender (M or F), and Phone Number - Use Commas to Separate Entries: ").split(",")
    firstNames.append(w.strip())
    lastNames.append(x.strip())
    genders.append(y.strip())
    phoneNumbers.append(z.strip())

for num in range(int(numberContacts)):
    firstName=firstNames[num]
    lastName=lastNames[num]
    gender=genders[num]
    phoneNumber=phoneNumbers[num]

    #DISPLAY NAMES    
    pen.color("black")
    pen.up()
    pen.setpos(xpos,ypos-25)

  
    pen.down()
    pen.write(firstName + " " + lastName,font=style)
    pen.up()

    #DISPLAY PHONE NUMBER
    pen.sety(ypos-50)
    pen.down()
    pen.write(phoneNumber,font=style)
    pen.up()

    #DRAW FIGURE  
    pen.setx(xpos+50)
    pen.sety(ypos-100)
    
    pen.down()
    if gender.upper() == "M":
        draw_man()
    elif gender.upper() == "F":
        draw_woman()
    else:
        pen.write("X",font=style)
    pen.up()

    #move over for next contact    
    xpos+=(winwidth/numberContacts)
            
turtle.done()
