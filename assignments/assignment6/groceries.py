# Author: Gatlin Lawson

print("Welcome to our grocery store")

fruits = [ "apples", "bananas", "pears", "grapes", "kiwis"]

print("The following items are in the store: ")

                
for fruit in fruits:
    print("- " + fruit)        
choice = input("What would you like to order? ")
if choice in fruits:
    print(f"We've ordered {choice} for you")
    fruits.remove(choice)
else:
    print(f"Sorry we don't have any {choice}")

print("Now the grocery store contains the following: ")
for fruit in fruits:
    print("- " + fruit)

print("Goodbye")       