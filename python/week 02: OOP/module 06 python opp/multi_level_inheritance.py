class vehicle:
    def __init__(self,name,price) -> None:
        self.name = name
        self.price = price
    
    def __repr__(self) -> str:
        return f'{self.name}{self.price}'
    
    def move(self):
        pass

class bus(vehicle):
    def __init__(self, name, price,seat) -> None:
        self.seat = seat
        super().__init__(name, price,)
    def __repr__(self) -> str:
        # return self.seat
        return super().__repr__()

class Truck(vehicle):
    def __init__(self, name, price,weight) -> None:
        self.weight= weight
        super().__init__(name, price)
class pickupTruck(Truck):
    def __init__(self, name, price, weight) -> None:
        super().__init__(name, price, weight)

class ACbus(bus):
    def __init__(self, name, price, seat,temperature) -> None:
        self.temperature = temperature
        super().__init__(name, price, seat)
    def __repr__(self) -> str:
        print(f'{self.seat}')
        return super().__repr__()

green_line = ACbus('green',5000000,22,16)
print(green_line)
ena = bus('ena',5000000,5)
print(ena)
print('-----')
print()