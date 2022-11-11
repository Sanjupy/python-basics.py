#list = used to store multiple items in a single variable
food=["pizza","choclate","hotdog","maggie","flesh"]

food[0]="mango"
print(food[0])

food.append("ice cream")
print(food)
food.remove("hotdog")
food.pop()
food.insert(0,"cake")
for x in food:
    print(x)
