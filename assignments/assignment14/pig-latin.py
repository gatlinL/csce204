# Author: Gatlin Lawson

def is_vowel(letter):
    vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    if letter in vowel:            
        return True
    else:
        return False

def convert_to_pig_latin(word):
  flag = False
  vow_index = 0
  for i in range(len(word)):
      if (is_vowel(word[i])):
          vow_index = i
          flag = True
          break
      else:
        word = word[1:] + "-"+ word[0]+ "ay"
        break

  if not flag:
    return word
  pigLatin = word[vow_index:] + word[0:vow_index] + "-hay"
  return pigLatin
        
while True:
    command = input("(C)onvert or (Q)uit: ")
    if command == "q":
        break
    elif command == "c":
        word = input("Enter word: ")
        print(convert_to_pig_latin(word))
    else:
        print("Invalid command")

print("Goodbye")
