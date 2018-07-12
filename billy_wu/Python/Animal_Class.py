class Animal:
    def __init__(self,name,health=0):
        self.name = name
        self.health = health
    def walk(self):
        self.health = self.health - 1
        return self
    def run(self):
        self.health = self.health + 1
        return self
    def display_health(self):
        print(str(self.name) + "'s health is " + str(self.health))
        return self
cat=Animal("Meow",100)
cat.walk().walk().walk().run().run().display_health()

class Dog(Animal):
    def __init__(self,name,health):
        super(Dog,self).__init__(name,health)
        self.name = name
        self.health = 150
    def pet(self):
        self.health = self.health + 5
        return self
dog=Dog("Boomer",100)
dog.walk().walk().walk().run().run().pet().display_health()

class Dragon(Animal):
    def __init__(self,name,health):
        super(Dragon,self).__init__(name,health)
        self.name = name
        self.health = 170
    def fly(self):
        self.health = self.health - 10
        return self
    def display_health(self):
        print("I am a dragon!")
        return self
dragon=Dragon("Puff",100)
dragon.display_health()

# bunny=Animal("Fluffers",25)
# bunny.fly()
# bunny.pet()
# bunny.display_health()
# dog.fly()
