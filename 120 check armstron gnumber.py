n=int(input("enter the number:"))   #n=153
s=n
b=len(str(n))
sum1=0
while n!=0:  #153    n=15   n=5 n= 1
    r=n%10   #153%10  15%10=5  1%10  
    sum1=sum1+(r**b)  #3**3=27   5**3=125  1**3  
    n=n//10  #153//10=15 so in the loop n =(is 15)  for third iteration n is 1
if s==sum1:
    print("number is armstrong")
else:
    print("not armstrong")

