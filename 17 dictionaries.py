#dictionary=chamgable unordered collections

#key value type is dictionary
capitals={"usa":"washington",
            "inida":"new delhi",
            "china":"bejjing"}

capitals.update({"germany":"berlin"})
capitals.update({"usa":"losvegas"})
capitals.pop('china')

print(capitals["usa"])

print(capitals.get("germany"))
print(capitals.keys())
print(capitals.values())
print(capitals.items())

for key,Value in capitals.items():
    print(key,Value)



