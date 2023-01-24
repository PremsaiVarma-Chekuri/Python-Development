class Cart:
    def __init__(self,basket):
        self.basket = basket
        self.items = {"Milk":85,"Vegetables":200,"Fruits":300}
        self.amount = 0
    def total_amount(self):
        for i in self.basket:
            self.amount+=self.items[i]
        return self.amount
cart1 = Cart(["Milk","Fruits"])
cart2 = Cart(["Vegetables","Fruits"])
print(cart1.total_amount())
print(cart2.total_amount())
        