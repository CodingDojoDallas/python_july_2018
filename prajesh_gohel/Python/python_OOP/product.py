import sys

class Product:

    def __init__(self, price, name, weight, brand, status="for sale"):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status = status

    def sell(self):
        self.status = "sold"
        return self

    def addTax(self, tax=.08):
        hold = self.price * tax
        self.price = self.price + hold
        return self

    def returnItem(self, reason_for_return):
        if reason_for_return == "defective":
            self.status = "defective"

        elif reason_for_return == "like new":
            self.status = "for sale"

        elif reason_for_return == "opened":
            self.status = "used"
            self.price = self.price*.8

        return self

    def displayInfo(self):
        print("\nPrice:", self.price, "\nName:", self.name, "\nWeight:", self.weight, "\nBrand:", self.brand, "\nStatus:", self.status)

pokemon_cards = Product(4, "Pokemon Booster Pack", ".5lb", "Nintendo")
pokemon_cards.returnItem("opened").displayInfo()
