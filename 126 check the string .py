import re

def is_allowed(string):
    char=re.compile(r'[^a-zA-Z0-9]')
    string=char.search(string)
    return  not bool(string)

print(is_allowed("1"))
