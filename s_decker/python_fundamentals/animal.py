class Animal:

	def __init__(self, name, health):
		self.name = name
		self.health = health
	def walk(self):
		self.health = self.health - 1
		return self
	def run(self):
		self.health = self.health - 5
		return self
	def displayHealth(self):
		print(str(self.health))
		return self

cat = Animal("Kitty", 50)

cat.walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
	def __init__(self, name):
		super().__init__(name, 150)

	def pet(self):
		self.health = self.health + 5
		return self

dog = Dog("Spot")

dog.walk().walk().walk().pet().fly().displayHealth()

class Dragon(Animal):
	def __init__(self, name):
		super().__init__(name, 170)

	def fly(self):
		self.health = self.health - 10
		return self

	def displayHealth(self):
		super().displayHealth()
		print("I am a dragon")
		return self

dragon = Dragon("Puff")

dragon.fly().displayHealth()

class Lizard(Animal):
	def __init__(self, name):
		super().__init__(name, 35)

lizzie = Lizard("Elizabeth")

lizzie.fly().pet().displayHealth()