# static attrabute (class attribute)
# static method @staticmethod
# class method @classmetod
# defferances between static method and class method
class Shoping:
    cart = [] # class sttribute # static attribute
    origin = 'china'
    def __init__(self,name,location) -> None:
        self.name = name
        self.location = location
    def purchas(self,item,price,amount):
        remaining = amount - price
        print(f'buying : {item} for price: {price} and remaining: {remaining}')
    
    @staticmethod
    def multiply(a,b):
        rasult = a*b
        print(rasult)
    
    @classmethod
    def hudai_dkhi(self,item):
        print('hudai dekhi kintu kinmu just ac ar hawa khaita aschi',item)
basundara = Shoping('basu en dhara','not popular location')
basundara.purchas('longi', 500,1000)
basundara.hudai_dkhi('longi')
Shoping.purchas(2,2,3,3)
Shoping.hudai_dkhi('lingi')
Shoping.multiply(6,7)