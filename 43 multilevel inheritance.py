#multilevel inheritances =child class to child class

from operator import truediv


class Organism:
    alive=True

class Animal(Organism):
    def eat(Self):
        print("this animal is eating")

class Dog(Animal):
    def bark(Self):
        print("this dog is barking")
dog=Dog()
print(dog.alive)
dog.bark()
dog.eat()

animal=Animal()

animal.eat()
print(animal.alive)
