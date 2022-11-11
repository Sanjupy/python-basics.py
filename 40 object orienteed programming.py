from pyexpat import model
from turtle import color


class Car:

    
    def __init__(self,make,model,year,color):
        self.make="chevy"
        self.model="corvette"
        self.year=2021
        self.color="red"

    def drive(Self):
        print("the car is driving")

    def stop(Self):
        print("the car stopped")

car_1=Car("chevy","corvette",2021,"blue")

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)
print(car_1.drive)
print(car_1.stop)