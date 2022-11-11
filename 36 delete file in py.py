import os
try:
    os.remove("sanju.txt")
except FileNotFoundError:
    print("no file idiot")
except PermissionError:
    print("no permission")
