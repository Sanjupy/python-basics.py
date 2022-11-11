from ast import Slice
import http


name="sanjeevkumar"
first_name=name[0:7]
last_name=name[7:12]
print(first_name)
print(last_name)

funky_name="kanewilliamson"
key_name=funky_name[0:14:2]

print(key_name)

reversed_name=name[7:12]
print(reversed_name)

website="http://google.com"
slice=slice(7,-4)
print (website[slice])
