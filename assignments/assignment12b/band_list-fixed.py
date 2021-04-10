# Author: Gatlin Lawson

bandsFile = "assignments/assignment12b/bands.txt"

def writeBands(bands):
    with open(bandsFile, "w") as file:
        for band in bands:
            file.write(band + "\n")

# Command to read through txt file
def readBands():
    bands = []
    with open(bandsFile) as file:
         for line in file:
             line = line.replace("\n","").strip()
             bands.append(line)
    return bands

# Command to list bands
def listBands(bands):
    for i in range(len(bands)):
        print(f"{i+1}. {bands[i]}")

# Command add band list
def addBands(bands):
    band = input("Band: ").strip().lower()   
    if band in bands:
        print(f"Sorry, {band} is already on the list")
    elif band not in bands:
        bands.append(band)
        writeBands(bands)
        print(f"{band} was added")
        return bands

# Command delete band list
def deleteBand(bands):
    deleteAnswer = input("Enter Band: ").strip().lower()
    if deleteAnswer not in bands:
        print(f"Sorry, {deleteAnswer} was not found on the list")
    elif deleteAnswer in bands:
        band = bands.remove(deleteAnswer)
        writeBands(bands)
        print(f"{deleteAnswer} was deleted")
    return bands
while True:
    bandEntry = input("Enter (L)ist, (A)dd, (D)elete, or (Q)uit: ").lower().strip()
    bands = readBands()

    if bandEntry == "q":
        break
    elif bandEntry == "l":
        listBands(bands)
    elif bandEntry == "a":
        bands = addBands(bands)
    elif bandEntry == "d":
        bands = deleteBand(bands)
    else:
        print("Invalid command, try again")

               
print("Goodbye")

