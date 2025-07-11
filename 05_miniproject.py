print("--------------------🧠 Welcome To The Python Quiz!--------------------------")
score = 0
#Question 1
q1=input("Q1.Whai is The Data Type of True in Python? ")
if q1.lower()=='boolean':
    score +=1
#Question 2
q2=input("Q2.What Function is used to Take User Input?" )
if q2.lower()=='input':
    score +=1
#Question 3
q3=input("Q3.What is The Data Type of 'Rahul' in Python?")
if q3.lower()=='string':
    score+=1
#Result
print(f"\n you got{score}/3 is correct!")
if score == 3:
    print("Excellent! you're a python pro.")
if score ==2:
    print("Good job,Keep practicing")
else:
    print("Keep learning.you got this!")