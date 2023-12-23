#Create a Product class and a Shop class.
class poduct:
    def __init__(self,P_name,quentity,price) -> None:
        self.P_name = P_name
        self.quentity = quentity
        self.price = price

class shop(poduct):
    def __init__(self,name, P_name, quentity, price) -> None:
        self.name = name
        super().__init__(P_name, quentity, price)
    # def __init__(self,name,) -> None:
    #     self.name = name
    #     poduct.__init__(self,p_name,))
    def detels(self):
        print("shop name : ",self.name,"product name : ",self.P_name,"quentity : ",self.quentity,"price",self.price)
alo = poduct("mola",22,1200)
sopnosupershop = shop("shopno", 'kola',45,'700usd')

sopnosupershop.detels()