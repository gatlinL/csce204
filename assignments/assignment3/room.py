# Author: Gatlin Lawson
import math

#Measurements of room
print("Let's finish your room")
width = float(input("Room Width: "))
length = float(input("Room Length: "))
height = float(input("Room Height: "))

#Square foot flooring, insulation, and drywall ceiling
squareFoot = length * width
#Square foot drywall walls (4)
squareFoot1 = (length * height) * 2 + (width * height) * 2

#Cost
flooring = squareFoot * 1.5
insulate = squareFoot * 0.5
drywallCeiling = squareFoot * 2
drywallWall = squareFoot1 * 2
#Total Cost
totalCost = flooring + insulate + drywallCeiling + drywallWall

print(f"Room finishing cost: ${totalCost} ")