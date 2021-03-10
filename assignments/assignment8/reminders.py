# Author: Gatlin Lawson

from datetime import time 

appointments = {"Weight Lifting": time(hour=7,minute=40,),
                "Pick up breakfast": time(hour=8,minute=45),
                "Dentist appointment": time(hour=10,minute=00),
                "Lunch at the house": time(hour=12,minute=00),
                "School work": time(hour=1,minute=00),
                "Take a nap": time(hour=2,minute=15),
                "Track practice": time(hour=3,minute=30),
                "Hot tub": time(hour=5,minute=15),
                "Dinner": time(hour=6,minute=30),
                "More school work": time(hour=8,minute=00),
                "Bedtime": time(hour=10,minute=00)}

#print(appointments)

counter = 1

for appointment in appointments:
    schedule = appointments[appointment]
    print(f"{counter}. {appointment} - " + schedule.strftime("%I:%M %p"))
    counter += 1