#method over ride is to over ride a method from parent class to child class
class Animal():
    def eat(self):
        print("the animal eats")

class Rabbit(Animal):
    def eat(Self):
        print("the rabbit does not eat")

rabbit=Rabbit()

rabbit.eat()


