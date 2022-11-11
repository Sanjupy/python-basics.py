import os

source=" text.txt"
destination="C:\\Users\\mangu\\OneDrive\\Desktop\\folder"
try:
    if os.path.exists(destination):
        print("there is file")
    else:
        os.replace(source,destination)
        print(source+"was moved")

except FileNotFoundError:
    print(source+"not found")