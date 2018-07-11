class Product:

	def __init__(self, price, name, weight, brand, status="For Sale"):
		self.price = price
		self.name = name
		self.weight = weight
		self.brand = brand
		self.status = status

	def sold(self):
		self.status = "sold"
		return self

	def addtax(self):
		self.price = self.price+self.price*0.1
		return self

	def returned(self):
		if self.status=="defective":
			self.price=0
		elif self.status=="like_new":
			self.status = "For Sale"
		elif self.status=="opened":
			self.status="Used"
			self.price=self.price*.8
		return self

	def displayInfo(self):
		print("Price: $" + str(self.price))
		print("Item Name: " + self.name)
		print("Weight: " + str(self.weight) + "lbs")
		print("Brand: " + self.brand)
		print("Status: " + self.status)
		return self

cup=Product(1.00, "Reases Cups", 0.3, "Hershee")
bar=Product(1.25, "Hershee Bar", 0.25, "Hershee")
car=Product(210.00, "Landspeeder", 75.3, "SW")
can=Product(.50, "LaCross", .01, "Drink Me", "defective")

can.returned().displayInfo()
car.addtax().displayInfo()
cup.sold().displayInfo()