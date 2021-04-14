# Author: Gatlin Lawson

from bird2 import Bird

def get_birds():
    birds = []

    with open("Assignments/assignment13b/birds.txt") as file:
        for line in file:
            data = line.split(',')
            bird_type = data[0].strip().capitalize()
            color = data[1].strip().lower()
            food = data[2].strip().lower()
            description = data[3].strip().lower()
            birds.append(Bird(bird_type, color, food, description))
    return birds

birds = get_birds()

print("Bird Program!!!")

while True:
    command = input("(L)ist all birds, get a birds (D)etails, or (Q)uit: ").lower().strip()

    if command == "l":
        for bird in birds:
            bird.display()
    elif command == "d":
        bird_name = input("Enter bird name: ").strip().capitalize()
        for bird in birds:
            if bird.is_match(bird_name):
                bird.display()
    elif command == "q":
        break
    else:
        print("Invalid command")

print("Goodbye")