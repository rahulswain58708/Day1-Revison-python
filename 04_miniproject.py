'''4. Movie Ticket Price Calculator
Ask user for age and day of the week.

Charge differently based on age group and discount on Sunday.'''
age=int(input("Enter your age : "))
day=input("Enter the day of the week : ")
if age<13:
    price = 100
if age<18:
    price = 1500
if age<60:
    price = 200
else:
    price = 120
# Apply Sunday discount
if day == "Sunday":
    discount = 0.20
    price -= price * discount
#output final price
print(f"your ticket price is:₹{price} ")