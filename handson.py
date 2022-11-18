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
class groceryItem(Product):
    def __init__(self, name, price, deal_price, rating, expiry_date):
        super().__init__(name, price, deal_price, rating)
        self.expiry_date = expiry_date
    def get_expiry_date(self):
        return self.expiry_date
    def get_item_details(self):
        super().display_product_details()
        print("Expiry date: {}".format(self.expiry_date))

class Order:
    delivery_charges={
        "prime_member":0,
        "non_prime_member":50
    }
    def __init__(self,delivery_type,location):
        self.items = []
        self.delivery_tyoe = delivery_type
        self.location = location
    def add_items(self,product,quantity):
        self.items.append((product,quantity))
    def display_order_details(self):
        print("-----------------Product---------------------")
        for product,quantity in self.items:
            product.display_product_details()
            print("Quantity: {}".format(quantity))
            print("-----------------")



tv = electronicItem("TV",40000,35000,4.7,12)
keyboard = electronicItem("Logitach Keyboard",10000,5000,4.5,12)
mouse = electronicItem("Logitach Mouse",5000,4000,4,12)
milk = groceryItem("Milk",80,75,5,"10 days")
flour = groceryItem("Flour",150,120,4.5,"1 year")
order = Order("prime","Hyderabad")
order.add_items(tv,1)
order.add_items(keyboard,5)
order.add_items(mouse,9)
order.add_items(milk,10)
order.add_items(flour,2)
order.display_order_details()
"""x = pro.get_waranty()
print(x)"""


    