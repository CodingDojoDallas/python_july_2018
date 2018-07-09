class Animal:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def displayHealth(self):
        print("\n", "Health:", self.health)
        return self

class Dog(Animal):
    def __init__(self, name):
        self.health = 150

    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self, name):
        self.health = 170

    def fly(self):
        self.health -= 10
        return self

    def displayHealth(self):
        super().displayHealth()
        print("I am a Dragon!")
        return self

class Cheetah(Animal):
    def __init__(self, name):
        self.health = 160

    def sprint(self):
        self.health -= 8
        return self

    def displayHealth(self):
        super().displayHealth()
        print("I'm a Cheetah!")
        return self

test = Animal("Brandy")
test.walk().walk().walk().run().run().displayHealth()

poodle = Dog("Toodles")
poodle.walk().walk().walk().run().run().pet().displayHealth()

dragon = Dragon("Sparkles")
dragon.walk().fly().displayHealth()

cheetah = Cheetah("Spotz")
cheetah.walk().run().sprint().displayHealth()
