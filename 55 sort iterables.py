#sort()=used with list
#sort() function=used with iterables
#iterables are nothing but list tuples dict and sets and arrays

students=("sanju","mangu","kumar","sanjeev","curry")

#students.sort(reverse=True)
sorted_students=sorted(students,reverse=True)

for i in sorted_students:
    
    print(i)

students=[("sanju","f",60,
        "mangu","b",77,
        "kumar","c",99,
        "sanjeev","u",00,
        "curry","A",88)]
age=lambda ages:ages[1]
students.sort(key=age,reverse=True)
for i in students:
    print(i)

