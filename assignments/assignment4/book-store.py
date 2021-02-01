# Author: Gatlin Lawson

print("***** Welcome to our bookstore *****")
bookStore = input("What would you like to do (V)iew or (O)rder: ").lower().strip()


if bookStore == "v":
    print("""Our catalogue consist of: 
    - 1984 by George Orwell
    - The Help by Kathryn Stockett
    - Gone with the Wind by Margaret Mitchell
    - The Fellowship of the Ring by J.R.R Tolkien""")
elif bookStore == "o":
    input("Enter book name: ")
    if "1984":
        print("You can buy 1984 for $9.99")
    elif "The Help":
        print("You can buy The Help for $7.59")
    elif "Gone with the Wind":
        print("You can buy Gone with the Wind for $8.50")
    elif "The Fellowship of the Ring":
        print("You can buy The Fellowship of the Ring for $10.11") 

print("Have a nice day")
        

