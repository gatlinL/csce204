# Author: Gatlin Lawson

speed = float(input("Enter speed: "))
ticketPrice = 0

if speed >= 100:
    print("Time to stay overnight")
    ticketPrice = 20 * (speed - 70)
elif speed >= 90:
    print("Time for a ticket")
    ticketPrice = 10 * (speed - 70)
elif speed >= 80:
    print("Warning!")
elif speed > 70:
    print("Slow Down")
elif speed > 60:
    print("Good Job!")
elif speed > 50:
    print("Speed up")
else:
    print("Too slow time for a ticket")

if ticketPrice > 0:
    print(f"You are charged ${ticketPrice}")