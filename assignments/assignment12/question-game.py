# Author: Gatlin Lawson
import random
import os

from os.path import abspath, dirname

CURR_DIR = file_directory = dirname(abspath(__file__))

FILE_NAME_TRIVIA = "trivia.txt"
FILE_NAME_SCORE = "score.txt"

FILE_NAME_TRIVIA = os.path.join(CURR_DIR, FILE_NAME_TRIVIA)
FILE_NAME_SCORE = os.path.join(CURR_DIR, FILE_NAME_SCORE)


def getScores():
    with open(FILE_NAME_SCORE, 'r') as scorefile:
        lines = scorefile.readlines()
        if not lines:
            return 0
        return lines

def saveScores(scores):
    with open(FILE_NAME_SCORE, "w") as file:
        file.write(f"{scores[0]}\n")
        file.write(f"{scores[1]}\n")
        file.write(f"{scores[2]}\n")


# Reach each line of the file into a dictionary.  The dictionary will look like:
# Question -> Answer 
# We use a convert to bool method to convert "true" to True  
def getQuestions():
    questions = {}
    with open(FILE_NAME_TRIVIA) as file:
        for line in file:
            data = line.split(':')
            question = data[0].strip()
            answer = data[1].strip()
            questions[question] = convertToBool(answer)
        return questions

# Converts a string representation of a boolean to a Boolean
def convertToBool(answer):
    if answer == "true":
        return True
    else:
        return False

# Asks the user a random trivia question
# Gathers the users answer
# if their answer is the stored answer then return true (they won), otherwise return false
def playRound():
    question = random.choice(list(questions.keys()))
    userAns = input(f"True or False: {question} ").strip().lower()
    compAns = questions.get(question)

    if convertToBool(userAns) == compAns:
        return True
    else:
        return False

def displayCounts():
    print(f"Games Played: {scores[0]}")
    print(f"Games Won: {scores[1]}")
    print(f"Games Lost: {scores[2]}")


# Let's play the game - START HERE!
print("Welcome to our Trivia Game")
scores = getScores()
displayCounts()

# Load all the questions from the file
questions = getQuestions()

# Loop as long as the user wants to keep playing
while True:
    command = input("(P)lay or (Q)uit: ").strip().lower()
    
    # if they enter q, quit the game
    if command == "q":
        break
    # if they enter an invalid command, indicate that
    elif command != "p":
        print("Invalid command")
        continue
    
    # otherwise play a round, if playRound is true, they won
    # WON
    if playRound():
        scores[0] = int(scores[0]) + 1
        scores[1] = int(scores[1]) + 1       
        print("Yay, you got it!")
    #LOST
    else:
        scores[0] = int(scores[0]) + 1
        scores[2] = int(scores[2]) + 1
        print("Sorry, incorrect")


displayCounts()
saveScores(scores)
print("Goodbye")