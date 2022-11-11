#exception= events detected during the execution that interputs the flow of programme

from logging import exception


try:



    numerator=int(input("enter a number"))

    denomenator=int(input("enter a number"))

    result=numerator/denomenator
    print(result)
except ZeroDivisionError as e:
    print(e)
    print("u cant divide by zero")

except ValueError as e:
    print(e)
    print("cant divide by str")

except Exception as e:
    print(e)


    print("something went wrong:")
else:
    print(result)

finally:
    print("this will always exceute")

