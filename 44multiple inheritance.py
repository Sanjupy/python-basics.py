class Prey():
    def flee(self):
        print("this animal flees")

class Predetor():
    def hunt(self):
        print("this animal hunts")

class Rabbit(Prey):
    pass

class Hawk(Predetor):
    pass

class Fish(Prey,Predetor):
    pass


rabbit=Rabbit()
fish=Fish()
hawk=Hawk()

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()

