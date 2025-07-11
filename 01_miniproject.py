#🚀 Mini Project: Student Info System

name=input("Enter your name: ")
roll_no=int(input("Enter your Roll No: "))
age=int(input("Enter your age: "))
marks=[]
for i in range(1,6):
    mark=int(input(f"Enter marks for subject{i}: "))
    marks.append(mark)
total=sum(marks)
percentage=round((total/600)*100,2)
# Grade logic
if percentage>=90:
    grade="A"
elif percentage>=75:
    grade="B"
elif percentage>=50:
    grade="c"
else:
    grade="Fail"
#output
print("----------------------------------------STUDENT REPORT CARD--------------------------------------------------")
print(f"Name        :{name}")
print(f"age         :{age}")
print(f"Roll No     :{roll_no}")
print(f"Total       :{total}/600")
print(f"percentage  :{percentage}%")
print(f"Grade       :{grade}")
print("------------------------------------------------------------------------------------------------------------------")