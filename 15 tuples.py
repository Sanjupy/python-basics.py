#tuple=collection which is ordered and un changable 
#tuples are immutable
student=("sanju",21,"male","sanju")

print(student.count("sanju"))
student.index("male")

for x in student:
    print(x)


if "sanju" in student:
    print("sanju is hero")
