from abc import ABC,abstractclassmethod
class Animal(ABC):
    # card = []
    def __init__(self,name,age) -> None:
        self.name = name
        self.age= age
        super().__init__()
    @abstractclassmethod
    def all_name(self):
        return f"halar po kan daksos I am {self.name}"
    def aha(self):
        return "nathing else"
class mankey(Animal):
    def __init__(self, name, age,eat) -> None:
        self.eat = eat
        super().__init__(name, age)
    def __repr__(self) -> str:
        return "king is back"
    def all_name(self):
        pass
hoki = mankey("moli",3,"bamobo")

print(hoki)
hoki.all_name()