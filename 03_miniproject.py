'''2. Age in Seconds Calculator
Ask user for age in years.

Calculate and show how many seconds they've lived.'''
age = int(input("Enter youre age : "))
# Approximate seconds in one year (365.25 days to account for leap years)
second_in_year=365.25*24*60*60
# Calculate total seconds lived
age_second=int(age*second_in_year)
# show result
print(f"you have lived approximoity {age_second} second.")

