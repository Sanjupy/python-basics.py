#set is unordered and unindexed.no duplicate vales

from lib2to3.pgen2.tokenize import untokenize


utensils={"fork","spoon","knife","knife","spoon"}
dishes={"bowl","cup","plate","knife"}

utensils.add("napkin")
utensils.remove("fork")
#utensils.clear()
dishes.update(utensils)
dinner_table=utensils.union(dishes)
for x in dinner_table:
    print(x)

print(dishes.difference(utensils))
print(dishes.union(utensils))

