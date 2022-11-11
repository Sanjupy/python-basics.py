#abstract calss==one or more abstract class
##prvents a user from creating object
#abstract method=has decleration but no implementation

from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def go(Self):
        pass

    @abstractmethod
    def stop(Self):
        pass


   

class Car(Vehicle):
    def go (self):
        print("u drive car")
    
    def stop(Self):
        print("the car stopped")

class Motorcycle(Vehicle):
    def go(self):
        print("u drive motor cycle")
    def stop(Self):
        print("the car stopped")

#vehicle=Vehicle()
car=Car()
motorcycle=Motorcycle()

#vehicle.go()
car.go()
motorcycle.go()
car.stop()
motorcycle.stop()