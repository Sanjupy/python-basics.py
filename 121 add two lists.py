list1=[1,2,3]
list2=[5,6,7]
list1=list1[0]+list1[1]+list1[2]
list2=list2[0]+list2[1]+list2[2]

list3=list1+list2
print(list1)
print(list2)
print(list3)


#6+18=24
def sum(numbers):
    total=0
    for x in numbers:
        total+=x
    return total
print(sum([1,2,3,4]))
