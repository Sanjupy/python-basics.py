#filter()=creates a colection of elements from an iterable for which function returns
#filter(function,iterable)

friends=[("sanju",19),
        ("saa",22),
        ("aaa",11)]

age=lambda data:data[1]>=18

drinking_buddies=list(filter(age,friends))
for i in drinking_buddies:
    print(i)