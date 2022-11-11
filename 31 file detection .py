
from genericpath import isfile
import os 

path="C:\\Users\\mangu\\OneDrive\\Desktop\\test.txt"

if os.path.exists(path):
    print("that location exist")
    if os.path.isfile(path):
        print("it is file")

else:
    print("no location exits")
