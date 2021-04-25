# Author: Gatlin Lawson

def replace_stars():
    answer = ""

    global word
    for letter in word:
        if letter == "*":
            answer += "."
        else:
            answer += letter
    
    word = answer

word = "a*b*c*d*"
answer = replace_stars()
print(word)