class Bike:
    def __init__(self,price,max_speed,miles=0):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    def displayInfo(self):
        print(self.price, self.max_speed, self.miles)
        return self
    def ride(self):
        print("Riding!")
        self.miles=self.miles+10
        return self
    def reverse(self):
        if self.miles>5:
            self.miles=self.miles-5
        else:
            print("You've been too lazy to reverse!")
            return self
        print("Reversing!")
        return self

bmx=Bike(100,"30mph")
huffy=Bike(200,"25mph")
cheese=Bike(250,"15mph")
bmx.ride().ride().ride().reverse().displayInfo()
huffy.ride().ride().reverse().reverse().displayInfo()
cheese.reverse().reverse().reverse()

# A if/else statement would prevent negative miles
# All of the methods need a return self to allow chaining methods