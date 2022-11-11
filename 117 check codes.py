punctuations="!@#$%,,,"
my_str=input("enter the string")

new_str=""

for c in my_str:
    if c not in punctuations:
        new_str+=c
print(new_str)

