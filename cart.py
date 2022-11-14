## Developing a cart providing adding items and displaying it and added parent class
class Product:
    def __init__(self,name, price, deal_price, ratings):
        self.name = name
        self.price = price
        self.deal_price = deal_price
        self.ratings = ratings
        self.you_save = price-deal_price
    def display_product_details(self):
        print("Product: {}".format(self.name))
        print("Price: {}".format(self.price))
        print("Deal Price: {}".format(self.deal_price))
        print("You saved: {}".format(self.you_save))
        print("Ratings: {}".format(self.ratings))
product = Product("ASUS Laptop",90000,75000,4.7)
product.display_product_details()

## Added child class

class electronicItem(Product):
    def set_warranty(self,warranty):
        self.warranty = warranty
    def get_warranty(self):
        return self.warranty
    def display_electronic_details(self):
        self.display_product_details()
        print("Warranty: {}\n".format(self.warranty))
class groceryItem(Product):
    def set_expiry_date(self,expire_date):
        self.expire_date = expire_date
    def get_expire_date(self):
        return self.expire_date
    def display_grocery_items(self):
        self.display_product_details()
        print("Expiry date: {}\n".format(self.expire_date))
"""e = electronicItem(24)
print(e.get_warranty())"""
ele = electronicItem("TV", 50000, 45000, 4.3)
ele.set_warranty(24)
ele.display_electronic_details()
gro = groceryItem("Chocolate",2000,1800,4.8)
gro.set_expiry_date(12)
gro.display_grocery_items()

## Added Order class

class Order:
    def __init__(self,delivery_type,delivery_address):
        self.items = []
        self.delivery_type = delivery_type
        self.delivery_address = delivery_address
    def add_item(self,name,quantity):
        self.items.append((name,quantity))
    def display_items(self):
        for name, quantity in self.items:
            name.display_product_details()
            print("Quantity: {}".format(quantity))
milk = groceryItem("Milk",80,75,4.7)
laptop = electronicItem("Laptop",80000,72000,4.5)

add = Order("Prime","Visakhapatnam")
add.add_item(milk,4)
add.add_item(laptop,1)
add.display_items()


