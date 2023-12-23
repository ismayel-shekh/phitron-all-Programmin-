class gadaget:
    def __init__(self,name,color,price) -> None:
        self.name = name
        self.color = color
        self.price = price
    def __repr__(self) -> str:
        return f"name {self.name}\n color {self.color}\n price {self.price}"
class laptop(gadaget):
    def __init__(self, name, color, price,ssd) -> None:
        self.ssd = ssd
        super().__init__(name, color, price)
class phone(gadaget):
    def __init__(self, name, color, price,ram) -> None:
        self.ram = ram
        super().__init__(name, color, price)
    def __repr__(self) -> str:
        return super().__repr__()
mobile = phone("apple","blue",120000,8)
print(mobile)
    
