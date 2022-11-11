import random

x=random.randint(1,6)
y=random.random()
print(x)
print(y)

myList=["rock","paper","scissors"]

z=random.choice(myList)

print(z)

cards=[1,2,3,4,5,6,7,8,9,"jack","ace","spade"]
random.shuffle(cards)
print(cards)
