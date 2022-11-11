#lambda function=function written in 1 line using lambda keyword
#accepts any number of arguments but has one expression

from audioop import add


def double(x):
    return x*2

print(double(5))


double=lambda x:x*2
multiply=lambda x,y:x*y
print(double(5))
print(multiply(5,6))
add=lambda x,y,z:x+y+z
print(add(5,5,5))
