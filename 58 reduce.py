#reduce()=apply function to a iterable and reduce it to a single cumulative value
#perform function on first two elements and repeat the process untill one value remains
#reduce(function ,iterable)
from cgitb import reset
import functools
from math import factorial
from unittest import result
letters=["H","E","L","L","O"]
word=functools.reduce(lambda x,y,:x + y,letters)
print(word)

factorial=[5,4,3,2,1]
result=functools.reduce(lambda x,y,:x*y,factorial)
print(result)
