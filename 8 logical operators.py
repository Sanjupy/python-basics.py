# and or and not are logical operators
#and =both should be true
#or =any 
temp=int(input("what is the temp outside:?"))
if (temp>=0 and temp<=30):
    print("it is cool")
    print("wear sweater")

elif not (temp<0 or temp>30):
    print("its freezing")
    print("dont go out")


    