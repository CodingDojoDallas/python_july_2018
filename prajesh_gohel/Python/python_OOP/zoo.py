class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def addDog(self, name):
        self.animals.append( Dog(name) )
    def addDragon(self, name):
        self.animals.append( Dragon(name) )
    def displayHealth(self):
        self.health = 100
        print("-"*30, self.health, "-"*30)
    def printAllHealth(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.displayHealth()
class Dog(Zoo):
    def __init__(self, name):
        self.name = name
    def addDog(self, name):
        super().addDog()
        print("Dog", name, "added!")
class Dragon(Zoo):
    def __init__(self, name):
        self.name = name
    def addDragon(self, name):
        super().addDragon()
        print("Dragon", name, "added!")
zoo1 = Zoo("John's Zoo")
zoo1.addDog("Tracy")
zoo1.addDog("Doggy")
zoo1.addDragon("Draggy")
zoo1.addDragon("Dragoon")
zoo1.printAllHealth()
