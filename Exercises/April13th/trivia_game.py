# Author: Gatlin Lawson

from question import Question
import random

questions = (
    Question("What type of animal is a seahorse?", "Crustacean", "Arachnid", "Fish", "Shell", 2),
    Question("Which of the following dog breeds is the smallest?", "Dachshund", "Poodle", "pomeranian", "Chicuahua", 3),
    Question("What color are zebras?", "White with black stripes?", "Black with white stripes", "Both of the above", "None of the above", 1),
    Question("What existing bird has the largest wingspan?", "Stork", "Swan", "Condor", "Albatross", 3)
)

print("Welcome to our Trivia Game!")

while True:
    command = input("Would you like to (P)lay or (Q)uit: ").strip().lower()

    if command == "q":
        break
    if command != "p":
        print("Invalid input")
        continue

    question = random.choice(questions)
    print("\n" + question.prompt)
    question.display_answers()

    user_ans = int(input("Enter numerial answer: "))

    if question.is_correct(user_ans):
        print("Great Job!")
    else:
        print(f"Sorry, wrong answer, correct answer is: {question.correct_answer + 1}")

print("Goodbye")