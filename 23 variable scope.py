#scope=The region that a variable is recognized

from unicodedata import name

name="sanjeev"  #global variable or global scope avaiable inside and outside of function
def display_name():
    name="kumar" #local varible or scope available inside this function
    print(name)

display_name()
print(name)


