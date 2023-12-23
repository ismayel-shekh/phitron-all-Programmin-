# Inside the Shop class, create a method name 
# add_product which adds products using the Product class to the Shop class.
class product:
    def __init__(self,product_name,weight,price) -> None:
        self.product_name = product_name
        self.weight = weight
        self.price = price
class shop(product):
    def __init__(self,name) -> None:
        self.name = name
        self.card =[]
    def detels(self):
        print("shop name: ",self.name)

    def add_product(self):
        self.card.append(product)
    def product_detels(self):
        print("shop name: ", self.name)
        print("poduct name: ",self.product_name)
        print("weight: ",self.weight)
        print("price: ",self.price)
product1 = product("gnaja",25,1700)
product2 = product("yeaba",12,14000)

tong = shop("shopno",)
# tong.product_detels()
print(len(tong.card))
