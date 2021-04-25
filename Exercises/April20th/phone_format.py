# Author: Gatlin Lawson

# original phone format (803)-123-4567
# desired phone format 803.123.4567
def update_phone(phone):
    answer = ""

    for char in phone:
        if char == "(" or char == ")":
            continue
        elif char == "-":
            answer += "."
        else:
            answer += char
    
    return answer

phone = update_phone("(803)-123-4567")
print(phone)