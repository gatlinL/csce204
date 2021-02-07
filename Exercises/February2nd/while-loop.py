# Author: Gatlin Lawson

command = input("Do you want to say hello (y or n)? ").lower().strip()

while command == "y":
    print("hello")
    command = input("Do you want to say hello again (y or n)? ")

print("Goodbye")