#higher order function=accepts a function as argument or returns function 



def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text=func("hello")
    print(text)
hello(loud)
hello(quiet)


def divisor(x):  #higher order function
    def divident(y): 
        return y/x
    return divident #return function
divide=divisor(2)
print(divide(10))
