# Author: Gatlin Lawson

friends = ["Austin", "Zach", "Parker", "Bailey"]

with open("Exercises/April1st/friends.txt", "w") as file:
    for friend in friends:
        file.write(f"{friend}\n")