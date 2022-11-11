##kwargs=parameter that unpack all arguments into dictionary
#accept varying amount of keyword arguments


def hello(**kwargs):
    #print("hello" +kwargs['first']+" "+kwargs['last'])
    print("hello",end=" ")
    for key,value in kwargs.items():
        print(value,end=" ")
hello(title="mr",first="sanjeev",middle="mangu",last="kumar")

