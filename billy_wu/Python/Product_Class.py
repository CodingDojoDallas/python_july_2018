class Product:
    def __init__(self, price, item_name, weight, brand, status="For Sale"):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = status
    def display_all(self):
        print("Price: $", self.price)
        print("Item Name: ", self.item_name)
        print("Weight: ", self.weight)
        print("Brand: ", self.brand)
        print("Status: ", self.status)
        return self
    def sell(self,status):
        self.status = "Sold"
        return self
    def addtax(self,tax):
        self.price = self.price * (1+tax)
        print("$"+str(self.price))
        return self
    def returnItem(self,reason_for_return):
        if reason_for_return=="defective":
            self.status = "Defective"
            self.price = 0
            print(self.status)
            print("Price: $"+str(self.price))
            return self
        if reason_for_return=="like_new":
            self.status = "For Sale"
            print(self.status)
            return self
        if reason_for_return=="opened":
            self.status = "Used"
            self.price = self.price*0.8
            print(self.status)
            print("Price: $"+str(self.price))
            return self
item1=Product(50, "shirt", "3 lb", "Gucci")
item2=Product(75,"pants", "5 lb", "Structure")
# item1.addtax(0.12).returnItem("opened")
# item1.addtax(0.12).sell("sold").display_all()
# item1.returnItem("opened").addtax(0.15).display_all()
# item2.display_all()