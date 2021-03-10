# Author: Gatlin Lawson

from datetime import date, time, datetime, timedelta

holidays = {"New Years": date(2021, 1, 1),
            "Valentines Day": date(2021, 2, 14),
            "Today": date(2021, 3, 9),
            "Easter": date(2021, 4, 4),
            "Mothers Day": date(2021, 5, 9),
            "July 4th": date(2021, 7, 4),
            "Labor Day": date(2021, 9, 6),
            "Halloween": date(2021, 10, 31),
            "Christmas": date(2021, 12, 25)}

for holiday in holidays:
    holidayDate = holidays[holiday]
    today = date.today()
    daysLeft = today + timedelta(days = 30)
    numberDays = holidayDate - today
    
    if today > holidayDate:
        print(f"{holiday} - " + holidayDate.strftime("%m/%d/%y") + " Passed")
    elif today == holidayDate:
        print(f"{holiday} - " + holidayDate.strftime("%m/%d/%y") + " Today!")
    elif holidayDate <= daysLeft:
        print(f"{holiday} - " + holidayDate.strftime("%m/%d/%y") + f" only {numberDays} left ")
    else:
        print(f"{holiday} - "+ holidayDate.strftime("%m/%d/%y"))