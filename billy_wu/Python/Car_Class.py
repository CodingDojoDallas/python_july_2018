class Car:
    def __init__(self, price, speed, fuel, mileage=0):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        # self.tax = tax
        self.display_all()
    def display_all(self):
        print("Price: ", str(self.price))
        print("Speed: ", str(self.speed))
        print("Fuel: ", str(self.fuel))
        print("Mileage: ", str(self.mileage))
        print("Tax: ", self.salestax())
        return self
    def salestax(self):
        if self.price>10000:
            # print("0.15")
            return "0.15"
        else:
            # print("0.12")
            # return self
            return "0.12"
        # return self
bmw=Car(12000, '35mph', 'Full', '15mpg')
# bmw.salestax()
