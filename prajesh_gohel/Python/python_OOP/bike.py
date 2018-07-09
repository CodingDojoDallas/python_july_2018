class Bike:
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print("\nPrice of Bike:", self.price, "\nMax Speed:", self.max_speed, "\nTotal Miles:", self.miles, "\n")
        return self

    def ride(self):
        self.miles += 10
        print("Riding")
        return self

    def reverse(self):
        if self.miles > 5:
            self.miles -= 5

        else:
            print("Cannot Reverse!")
            return self

        print("Reversing")
        return self

Scooter_Dooter = Bike(2000000000, "600mph")
Scooter_Dooter.ride().ride().ride().reverse().displayInfo()

Galactic_Hero = Bike(70000000000, "11500mph")
Galactic_Hero.ride().ride().reverse().reverse().displayInfo()

Shodddy_Boi = Bike(20, "15mph")
Shodddy_Boi.reverse().reverse().reverse().displayInfo()
