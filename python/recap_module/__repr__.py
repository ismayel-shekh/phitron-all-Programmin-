class repr:
    def __init__(self,name,age) -> None:
        self.name = name
        self.x = age
    def __repr__(self) -> str:
        return f"i am  {self.name} i am {self.x}"
alo = repr("modon",82)
print(alo)
# without __repr__ function    == <__main__.repr object at 0x7f090ace2e10>