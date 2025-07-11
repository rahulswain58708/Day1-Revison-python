# varible shadowing
#What wilbe printedand why?
x=10 # you created a global variable named x,its value is now 10.
def change(): # you created a function called change.
    x=5 #This create a local variable x,only inside the function.
    #It doesnot change the global x=10
change()
print(x) # output:-10
