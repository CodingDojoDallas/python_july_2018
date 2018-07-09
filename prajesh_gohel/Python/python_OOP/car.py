class Car:
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 0.15

        else:
            self.tax = 0.12

    def displayAll(self):
        print("\nPrice:", self.price, "\nSpeed:", self.speed, "\nFuel:", self.fuel, "\nMileage:", self.mileage, "\nTax:", self.tax,)

bmw = Car(25000, "60mph", "Full", "25mpg")
bmw.displayAll()

cheap_carz = Car(70, "1mph", "Bruh, U Empty as Hell", "1mpg")
cheap_carz.displayAll()

toyota = Car(50000, "60mph", "Halfway", "27mpg")
toyota.displayAll()

honda = Car(40000, "60mph", "Full", "35mpg")
honda.displayAll()

ferrari = Car(1000000, "60mph", "Almost Empty", "25mpg")
ferrari.displayAll()

tesla = Car(30000, "60mph", "Infinite", "30mpc")
tesla.displayAll()
