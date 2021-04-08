# Author: Gatlin Lawson

#bands = ["Greenday", "All American Rejects", "Dirty Heads", "Sublime"]
bands = []
bandsFile = "assignments/assignment12b/bands.txt"

def writeBands(bands):
    #with open("assignments/assignment12b/bands.txt", "w") as file:
    with open(bandsFile, "w") as file:
        for band in bands:
            file.write(f"{band}\n")

# Command to read through txt file
def readBands():
    #with open("assignments/assignment12b/bands.txt", "r") as file:
    with open(bandsFile, "r") as file:
         for line in file:
             bands.append(line.strip().lower())

# Command to list bands
def listBands():
    readBands()
    for band in bands:
        print("- " + band.capitalize())

# Command add band list
def addBands(bands):
    #answer = input("Band: ")
    #with open("assignments/assignment12b/bands.txt", "a",)as file:
    with open(bandsFile, "a") as file:
        answer = input("Band: ").strip().lower()
        readBands()
        if answer in bands:
            print(f"Sorry, {answer} is already on the list")
        elif answer not in bands:
            file.write(f"{answer}\n")
            print(f"{answer} was added")

# Command delete band list
def deleteBand(bands):
    with open(bandsFile, "r+") as file:
        deleteAnswer = input("Enter Band: ").strip().lower()
        readBands()
        file.seek(0)
        for band in bands:
            if band != deleteAnswer:
                file.write(f"{band}\n")
                file.truncate()
                print(f"{deleteAnswer} was deleted")
            elif deleteAnswer not in bands:
                print("Sorry, {deleteAnswer} was not found on the list")
        
        #if deleteAnswer in bands:

while True:
    bandEntry = input("Enter (L)ist, (A)dd, (D)elete, or (Q)uit: ").lower().strip()

    if bandEntry == "q":
        break
    elif bandEntry == "l":
        listBands()
    elif bandEntry == "a":
        addBands(bands)
    elif bandEntry == "d":
        deleteBand(bands)
    else:
        print("Invalid command, try again")

        
        
print("Goodbye")
#listBands()
#readBands()
#deleteBand(bands)
#addBands(bands)
#print(f"- {bands}\n".strip())
