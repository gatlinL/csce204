# Author: Gatlin Lawson

from house import House
import turtle

turtle.setup(575,575)
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()

"""
myHouse = House("1 A Street", 0, 0, 50, "medium aquamarine", "hot pink", True, True, 3)
myHouse.draw(pen)
"""

houses = []
houses.append(House("1 A Street", -200, 0, 50, "medium aquamarine", "hot pink", True, True, 3))
houses.append(House("2 A Street", -100, 0, 50, "burlywood", "cyan", False, True, 3))
houses.append(House("3 A Street", 0, 0, 50, "medium orchid", "khaki", False, True, 3))
houses.append(House("4 A Street", 100, 0, 50, "sandy brown", "aquamarine", True, True, 3))
houses.append(House("5 A Street", 200, 0, 50, "light sky blue", "plum", True, True, 3))

for house in houses:
    house.draw(pen)


turtle.done()