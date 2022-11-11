#loop control 
#break
#continue
#pass
#break is stop loop from executing if something is wrong
#continue is to run the loop even if anything is wrong


from unicodedata import name

while True:
    name=input("enter the name:")
    if name !="":
        break


phone_number="9999-1111-111"
for i in phone_number:
    if i=="-":
        continue
    print(i,end="")


for i in range(0,21):
    if i==13:
        pass
    else:
        print(i)



