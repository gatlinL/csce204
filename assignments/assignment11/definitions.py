# Author: Gatlin Lawson

def getDictionary():
    dictionary = {}
    with open("assignments/assignment11/words.txt") as file:
        for line in file:
            data = line.split(':')
            word = data[0].strip()
            wordDef = data[1].strip()
            dictionary[word] = wordDef
        return dictionary

def getDefinition():
    wordChoice = input("Enter Word: ").lower()
    if wordChoice in wordDef:
        print(f"{wordChoice}: {wordDef[wordChoice]}")
    else:
        print(f"Sorry, {wordChoice} is not in our system")
        
def displayDictionary():
    for word in wordDef:
        print(f"{word}: {wordDef[word]}")

print("Welcome to our dictionary")

wordDef = getDictionary()
while True:
    answer = input("Would you like to (V)iew, (D)efine, or (Q)uit: ").lower()
    if answer == "q":
        break
    elif answer == "v":
        displayDictionary()
    elif answer == "d":
        getDefinition()
    else:
        print("Invlaid input")

print("Goodbye")