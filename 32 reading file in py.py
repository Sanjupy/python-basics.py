#with open("text.txt") as file :
 #   print(file.read())
#print(file.closed)



try:

    with open("text.tx") as file :
        print(file.read())
except FileNotFoundError:
    print("no file")
    
