
def function2():
    a = int(input("First number:"))
    b = int(input("Second number:"))
    c = int(input("Third number pls:"))
    d=a+b+c
    print("The sum of", a,",", b, "and", c, "is", d)
def function4():
    a = int(input("number 1"))
    b = int(input("number 2"))
    if a == b :
        print("a is equal to b")
    elif a > b : 
        print("a is larger than b")
    elif a < b :
        print("a is smaller than b")
    
start=input("Enter the function to be executed")
if start =="1":
    #Function 1
elif start =="2":
    #function2()
elif start=="3":
    #Function 3
elif start =="4":
    #Function 4
