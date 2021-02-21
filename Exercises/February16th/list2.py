# Author: Gatlin Lawson

toys = ["doll", "rope", "truck", "car", "shovel"]
print("Welcome you our toy store")

while True:
    command = input("(V)iew, (A)dd, (R)emove, (Q)uit: ").lower().strip()

    if command == "q":
        break
    elif command == "v":
        for toy in toys:
            print(f"- {toy}")
    elif command == "a":
        toy = input("Enter toy: ")
        toys.append(toy)
    elif command == "r":
        toy = input("Enter toy you want to remove: ")
        toys.remove(toy)
    else:print("Invalid command")

print("Goodbye")
