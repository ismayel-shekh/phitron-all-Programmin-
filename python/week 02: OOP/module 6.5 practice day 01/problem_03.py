class Product:
    def __init__(self, product_name, weight, price):
        self.product_name = product_name
        self.weight = weight
        self.price = price

class Shop:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_product(self, prod):
        self.cart.append(prod)

    def buy_product(self, product_name):
        for product in self.cart:
            if product.product_name == product_name:
                self.cart.remove(product)
                print(f"Congratulations! You have successfully bought {product_name}")
                return
        print(f"Sorry, {product_name} is not available in the cart.")

    def shop_details(self):
        print("Shop name:", self.name)
        print("Products in the cart:")
        for prod in self.cart:
            print("Product name:", prod.product_name)
            print("Weight:", prod.weight)
            print("Price:", prod.price)

# Create instances of Product
product1 = Product("ganja", 25, 1700)
product2 = Product("yeaba", 12, 140000)

# Create an instance of Shop
tong = Shop("shopno")

# Add products to the shop's cart
tong.add_product(product1)
tong.add_product(product2)

# Buy a product and display the result
tong.buy_product("ganja")
tong.buy_product("fancidil")

# Display shop details
tong.shop_details()
