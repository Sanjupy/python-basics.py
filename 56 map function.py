#map()=applies function to each iterables (list,tuples,etc)

from ast import Store


store=[("shirt",20.00),
        ("pants",20.00),
        ("jacket",20.00),
        ("socks",20.00)]

to_euros=lambda data :(data[0],data[1]*0.82)
to_dollars=lambda data :(data[0],data[1]/0.82)
store_euros=list(map(to_euros,store))
store_dollars=list(map(to_dollars,store))
for i in store_euros:
    print(i)
for i in store_dollars:
    print(i)
    