# Author: Gatlin Lawson

print("Welcome to your todo list")

chores = []
completed = []

while True:
    command = input("(V)iew, (A)dd, (R)emove, (Q)uit: ").lower().strip()

    if command == "q":
        break
    elif command == "v":
        command2 = input("View (T)odos or (C)ompleted items? ").lower().strip()
        if command2 == "t":
            if not chores:
                print("You have no todos")
            else:
                for chore in chores:
                    print(f"- " + chore)
            #print(f"- {chores}")
        elif command2 == "c":
            for complete in completed:
                print(f"- " + complete)
            if not completed:
                print("You have no done items")
    elif command == "a":
        todo = input("Enter todo: ")
        chores.append(todo)
    elif command == "r":
        rmtodo = input("Enter todo: ")
        if rmtodo in chores:
            chores.remove(rmtodo)
            completed.append(rmtodo)
        else:
            print(f"Sorry {rmtodo} is not in your list")
    else:
        print("Invalid command")  







print("Goodbye")