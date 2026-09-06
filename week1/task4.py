
# claculate the square root of complex number
import cmath

num = 2+3j
sqrt = cmath.sqrt(num)
print("The square root of {0} is: {1:0.2f} + {2:0.2f}j".format(num, sqrt.real, sqrt.imag))