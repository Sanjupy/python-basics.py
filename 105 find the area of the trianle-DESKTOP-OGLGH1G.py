#(s*(s-a)(s-b)(s-c))**0.5
a=float(input("enter a value"))
b=float(input("enter b value"))
c=float(input("enter c value"))
s=(a+b+c)/2

area=(s*(s-a)*(s-b)*(s-c))**0.5
print('The area of the triangle is %0.2f' %area) 


