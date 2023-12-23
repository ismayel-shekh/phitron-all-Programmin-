class shopping:
    def __init__ (self,name):
        self.name = name
        self.card = []
    def add_to_cart(self,item,price,quantity):
        product = {'item' : item,'price' : price,'quantity' : quantity}
        self.card.append(product)

    def chackout(self,amount):
        total =0
        for item in self.card:
            total += item['price'] * item['quantity']
        print('total price',total)
        if amount < total:
            print(f'please rovide {total - amount} more')
        else:
            extra = amount-total
            print(f'here is your items and extra money {extra}')
swapan = shopping('alan swapon')
swapan.add_to_cart('alu',50,6)
swapan.add_to_cart('dim',12,24)
swapan.add_to_cart('rice',50,5)
print(swapan.card)
swapan.chackout(600)
swapan.chackout(1600)