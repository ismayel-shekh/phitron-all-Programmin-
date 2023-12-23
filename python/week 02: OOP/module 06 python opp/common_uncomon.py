class Gadget:
    def __init__(self,brand,price,color,origin):
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin 

    def run(self):
        return f'runing laptop: {self.brand}'
class laptop:
    def __init__(self,memory,ssd) -> None:
        self.memory = memory
        self.ssd = ssd
    def coding(self):
        return f'leaning python and practicing'

class phone(Gadget):
    def __init__(self, brand, price, color, origin,dual_sim):
        self.dual_sim = dual_sim
        super().__init__(brand, price, color, origin)

    def phone_call(self,number,text):
        return f'sending sms to: {number},with: {text}'
    
    def __repr__(self) -> str:
        return f'phone: {self.brand} {self.price}{self.dual_sim}'
class Camara:
    def __init__(self,pixel) -> None:
        self.pixel = pixel
    def change_lens(self):
        pass

my_phone = phone('iphone',120000,'silver','china', True)
print(my_phone.brand)
print(my_phone)

