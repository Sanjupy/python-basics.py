class Animal:
    alive=True

    def eat(Self):
        print("this animal is eating")

    def sleep(self):
        print("this animal is sleeping")

class Rabbit(Animal):
    def run(self):
        print("this rabbit is ruuning")

class Fish(Animal):
    def swim(self):
        print("this fish is swimming")

class Hawk(Animal):
    def fly(self):
        print("this hawk is flying")

    

rabbit=Rabbit()
fish=Fish()
hawk=Hawk()

print(rabbit.alive)
fish.eat()
hawk.eat()
rabbit.sleep()
rabbit.run()
fish.swim()
hawk.fly()