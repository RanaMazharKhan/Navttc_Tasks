
#area of triangle
a=5
b=3
c=4

#semi_perimeter
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("The area of triangle is: %.2f" % area)