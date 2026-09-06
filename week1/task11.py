
#nested if else condition
i=int(input("Enter a number: "))
if i>0:
    print("The number is positive")
    if i>10:
        print("The number is greater than 10")
    else:
        print("The number is less than or equal to 10")
else:
    print("The number is negative")
    if i<-10:
        print("The number is less than -10")
    else:
        print("The number is greater than or equal to -10")