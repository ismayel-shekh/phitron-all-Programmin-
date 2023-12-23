class shoping:
    card = [] # class attribute / static attribute
    origin ='china'
    def __init__(self,name,location) -> None:
        self.name = name
        self.location = location
    def purcase(self,item,price,amount):
        remaining = amount - price
        print(f'buying: {item}\n for price: {price}\n remining: {remaining}')
    @staticmethod
    def satic_method(a,b):
        print( a*b)
    @classmethod
    def class_method(self,item):
        print("for test",item)
    
busundara = shoping('king',"is")
# busundara.purcase('king',5,10)
shoping.class_method('modon')
shoping.satic_method(4,5)