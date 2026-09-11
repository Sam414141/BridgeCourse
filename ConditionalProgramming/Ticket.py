age = int(input("Enter your age :"))
ticket_Price = 500
if age <= 12 :
    print(f"You got the 10% off your ticket price is {ticket_Price - (ticket_Price/100)*10}")
else :
    print(f"Your ticket price is :{ticket_Price}")