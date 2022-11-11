#args=pack all args into a tuple
# useful so that a function can accept a varying amount of arguments


def add(num1,num2):#num1 and num2 are arguments
    sum=num1+ num2 
    return sum
print(add(1,2))



def add(*args):#num1 and num2 are arguments
    sum=0
    args=list(args)
    args[0]=0
    for i in args:
        sum+=i
    return sum

print(add(1,2,3,4,4,4,4))

