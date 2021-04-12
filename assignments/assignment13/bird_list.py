# Author: Gatlin Lawson

from bird import Bird


bird_list = (
    Bird("Toucan", "black with an orange beak", "fruits, insects, and small lizards", "Belongs to a family of Ramphastidae, with a Portuguese name"),
    Bird("Kind Fisher", "Various blues, with a brown bottom", "Fish", "Found in forest in tropical regions, and like to live near rivers"),
    Bird("Swift", "Black and White", "Worms", "One of the fastest flying birds, and are locared in all continents"),
    Bird("Hornbill", "Black and White", "Fruits and Insects", "During nesting, the male brings about 24000 fruits for the female")
)


print("Bird Program!!!")

while True:
    command = input("(L)ist all birds, get a birds (D)etails, or (Q)uit: ").lower().strip()

    if command == "l":
        for bird in bird_list:
            bird.display()
    elif command == "d":
        bird_name = input("Enter bird name: ").capitalize()
        for bird in bird_list:
            if bird.is_match(bird_name):
                bird.display()
    elif command == "q":
        break
    else:
        print("Invalid command")

print("Goodbye")