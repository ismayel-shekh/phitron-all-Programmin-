class shop:
    shoping_mall = 'jamuna'
    def __init__(self,buyer):
        self.buyer = buyer
        self.card =[]
    def add_to_card(self,item):
        self.card.append(item)
Ismayel = shop('ismayel shekh')
Ismayel.add_to_card('shoe')
Ismayel.add_to_card('phone')
print(Ismayel.card)
Ifat = shop('ifat shekh')
Ifat.add_to_card('hat')
Ifat.add_to_card('watch')
print(Ifat.card)
shakil = shop('shakil khan')
shakil.add_to_card('fish')
shakil.add_to_card('meet')
print(shakil.card)
