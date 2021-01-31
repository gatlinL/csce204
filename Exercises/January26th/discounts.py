# Author: Gatlin Lawson

weekDay = input("Enter weekday: ").lower().strip()

if weekDay == "monday" or "mon":
    print("Moes Monday")
elif weekDay == "tuesday" or "tues":
    print("Taco Tuesday")
elif weekDay == "wednesday" or "wed":
    print("Wine Wednesday")
else:
    print("No deals today")