#ducktyping=it has both attributes of walk and duck 
#class of object is less important than the methods or attributes
#if it walks like a duck and quacks like a duck,then it must be duck
class Duck():
    def walk(self):
        print("the duck is walking")
    
    def talk(self):
        print("the duck is qwacking")


class Chicken():
    def walk(self):
        print("the chicekn is walking")
    def talk(self):
        print("the chicken is clucking")

class Person():
    def catch(self,duck):
        duck.walk()
        duck.talk()
        print("u caught the critter")

duck=Duck()
Chicken=Chicken()
Person=Person()

Person.catch(duck)
Person.catch(Chicken)