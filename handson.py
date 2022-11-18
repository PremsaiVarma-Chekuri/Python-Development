class Product:
    def __init__(self,name,price,deal_price,rating):
        self.name = name
        self.price = price
        self.deal_price =deal_price
        self.rating = rating
        self.saved_money = self.price - self.deal_price
    def display_product_details(self):
        print("Name: {}".format(self.name))
        print("Price: {}".format(self.price))
        print("Deal Price: {}".format(self.deal_price))
        print("Rating: {}".format(self.rating))
        print("Saved: {}".format(self.saved_money))
class electronicItem(Product):
    def __init__(self, name, price, deal_price, rating, waranty):
        super().__init__(name, price, deal_price, rating)
        self.waranty = waranty
    def get_waranty(self):
        return self.waranty
    def get_item_details(self):
        super().display_product_details()
        print("Warranty: {}".format(self.waranty))
pro = electronicItem("TV",40000,35000,4.7,12)
pro.get_item_details()
x = pro.get_waranty()
print(x)


    