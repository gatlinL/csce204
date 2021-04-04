# Author: Gatlin Lawson

numbers = [8,16,53,108]

with open("Exercises/April1st/numbers.txt","w") as file:
   for number in numbers:
       file.write(f"{number}\n") 