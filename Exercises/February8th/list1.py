# Author: Gatlin Lawson

toys = ["doll", "truck", "ball", "car", "skipping rope"]

toys.append("phone")
toys.remove("truck")

# loop thorugh and display all the toys
for i in range(len(toys)):
    print(toys[i])

for toy in toys:
    print(toy)