import math
#find (b^2-4ac)/2a

a=int(input("enter the value"))
b=int(input("enter the value"))
c=int(input("enter the value"))

sqrt=((b^2-4*a*c)/2*a)
#print(sqrt)

#find the value of first quadrant -b+sqrt and -b-sqrt
sqrt1=-b+sqrt
sqrt2=-b-sqrt
print(sqrt1)
print(sqrt2)