'''1. Simple Calculator App
Take two numbers and an operator (+, -, *, /) as input.

Display the calculated result.

Use if-else to handle operations.'''
print("--------------------------------Simple Calculator-------------------------")
numb1=float(input("Enter your First number : "))
numb2=float(input("Enter Second number : "))
operator=input("Enter your opearator(+,-,*,/,%,**,//) : ")
if operator=='+':
    print(f"The sum is {numb1+numb2}")
elif operator=='-':
    print(f"The Difference is {numb1-numb2}")
elif operator=='*':
    print(f"The multiplication is {numb1*numb2}")
elif operator=='%':
    print(f"The Moduls is {numb1%numb2}")
elif operator=='/':
    print(f"The Division is {numb1/numb2}")
elif operator=='//':
    print(f"The Floor Division is {numb1//numb2}")
elif operator=='**':
    print(f"Square of Two number{numb1**numb2}")
else:
    print("Wrong operator , Try Again.")
print("---------------------Thanks for calculating-------------------------------")
