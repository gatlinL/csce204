# Author: Gatlin Lawson

temp = int(input("Enter temperature: "))
percip = input("Enter (R)ain, (S)now, or (N)one: ").lower().strip()

if temp <= 40 and percip == "s":
    print("You need a snowsuit")
elif temp <= 40 and percip == "r":
    print("You need a sweater and rain jacket")
elif temp <= 40:
    print("You need to dress in layers")