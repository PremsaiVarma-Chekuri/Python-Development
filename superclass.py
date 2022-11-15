class Product:
    def __init__(self,name,price,deal_price,rating):
        self.name = name
        self.price = price
        self.deal_price = deal_price
        self.rating = rating
        self.save_money = self.price - self.deal_price
    def display_product_details(self):
        print("Name: {}".format(self.name))
        print("Price: {}".format(self.price))
        print("Deal price: {}".format(self.deal_price))
        print("Rating: {}".format(self.rating))
        print("Saved money: {}".format(self.save_money))
#cart = Product("Mac book",120000,95000,4.8)
#cart.display_product_details()
class ElectronicItem(Product):
    def __init__(self,name,price,deal_price,rating,warranty_date):
        super().__init__(name,price,deal_price,rating)
        self.warranty_date = warranty_date
    def display_electronic_items(self):
        self.display_product_details()
        print("Warranty: {}".format(self.warranty_date))
cart = ElectronicItem("Mac book",120000,95000,4.8,12)
#cart.add_warranty_date(12)
cart.display_electronic_items()