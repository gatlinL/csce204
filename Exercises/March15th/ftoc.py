# Author: Gatlin Lawson

def fahr_to_cels(farenheit):
    celsius = (farenheit - 32) * 5/9
    return celsius

def cels_to_fahr(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

def miles_to_kil(miles):
    kilometers = miles * 1.60934
    return kilometers

def kilo_to_miles(kilo):
    miles = kilo * 0.621371
    return miles

print("Conversion program")
command = int(input(f"""
Enter type of conversion:
1. farenheit to celsius
2. celsius to farenheit
3. miles to kilemeters
4. kilometers to miles
"""))

value = float(input("Enter value: "))

if command < 1 or command > 4:
    print("Sorry invalid command")
elif command == 1:
    result = fahr_to_cels(value)
    print(f"{value}F = {round(result,2)}C")
elif command == 2:
    result = cels_to_fahr(value)
    print(f"{value}C = {round(result,2)}F")
elif command == 3:
    result = miles_to_kil(value)
    print(f"{value} miles = {round(result,2)} kilometers")
elif command == 4:
    result = kilo_to_miles(value)
    print(f"{value} kilometers = {round(result,2)} miles")