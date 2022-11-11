#nested loops = inner loop will finish all iterations before finishing one iteration of the outer loop




rows=int(input("how many number of rows?:"))  #outer loop

coloumns=int(input("how many number of columns?:")) #inner loop

symbol=input("enter a symbol to use:")

for i in range(rows):
    for j in range(coloumns):
        print(symbol ,end="")
    print()

