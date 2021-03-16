# Author: Gatlin Lawson


print("Calculator")

def decimalToBinary(decimal):
    if decimal > 0:
        decimalToBinary((int)(decimal/2))
        print(decimal%2, end='')

while True:
    answer= input("Convert from Binary to Decimal (BtD) or from Decimal to Binary (DtB), or (Q)uit: ").lower()
    if answer == "q":
        print("Goodbye")
        break
    elif  answer == "btd":
        binaryInput = input("Enter binary number: ")
        binaryToDeciaml = int(binaryInput,2)
        print(binaryToDeciaml)
    elif answer == "dtb":
        decimal = int(input("Enter decimal number: "))
        #dectobin(decimal)
        print (decimalToBinary(decimal)) 
    else:
        print("Invalid Command")
 



