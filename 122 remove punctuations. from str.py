#first enter the my_str which we have to enter in the terminal
my_str=input("enter the string")
#give the punctuations which we have to remove
punctuations="@!#$%^&,,..//??//"
#this is the output string which we will get
new_str=""
for c in my_str: #c is the temporary variable 
    if c not in punctuations: #if the punctuations are not there in c that will only be added to new_str
        new_str+=c            #the punctuations not there will only be added to new_str
print(new_str)
