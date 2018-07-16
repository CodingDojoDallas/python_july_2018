class Bike:
	def __init__(self, price, max_speed, miles):
		self.price = price
		self.max_speed = max_speed
		self.miles = miles
	def displayInfo(self):
		print("Price is $" + str(self.price))
		print("Speed " + str(self.max_speed))
		print("Mileage " + str(self.miles))
		return self
	def ride(self):
		print("Riding")
		self.miles=self.miles+10
		return self
	def reverse(self):
		print("Reversing ")
		self.miles=self.miles-5
		if self.miles < 0:
			self.miles = 0
		return self

storm = Bike(500,"20mph",0)
unicycle = Bike(350,"15mph",15)
blueberry = Bike(625,"37mph",0)

storm.ride().ride().ride().reverse().displayInfo()
unicycle.ride().ride().reverse().reverse().displayInfo()
blueberry.reverse().reverse().reverse().displayInfo()