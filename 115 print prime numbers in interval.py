lower=int(input("enter the first num"))
upper=int(input("enter the last num"))

print("the prime numbers in the range of ")
for number in range(lower,upper+1):
    if number > 1:
        for num in range(2,number):
            if(number%num)==0:
                break
        else:
            print(number)

        