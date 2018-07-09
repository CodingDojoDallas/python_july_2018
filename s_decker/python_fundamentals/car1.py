class Car:
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		if price > 10000:
			self.tax = .15
		else:
			self.tax = 0.12
		self.display_all()
		
	def display_all(self):
		print("Price: $" + str(self.price))
		print("Speed " + str(self.speed)+"mph")
		print("Fuel " + (self.fuel))
		print("Mileage " + str(self.mileage)+"mpg")
		print("Tax " + str(self.tax))
		return self

mini = Car(2000, 35, "Full", 15)
vw = Car(30000, 85, "Not Full", 45)
bmw = Car(50000, 95, "Full", 23)
ford = Car(8000, 55, "Full", 20)
chevy = Car(9000, 50, "Not Full", 20)
prius = Car(12000, 73, "Not Full", 52)

# mini.display_all()
# vw.display_all()
# bmw.display_all()
# ford.display_all()
# chevy.display_all()
# prius.display_all()
