from math import pi
class shape:
    def __init__(self,name) -> None:
        self.name = name
class rectangel(shape):
    def __init__(self, name,length,width) -> None:
        self.length = length
        self.width = width
        super().__init__(name)
    def ara(self):
        return self.length * self.width
class circle(shape):
    def __init__(self, name,radius) -> None:
        self.radius = radius
        super().__init__(name)
    def ara(self):
        print("pi value : ",pi)
        return pi * self.radius * self.radius
alo = rectangel('boom',5,4)
print(alo.ara())
kodo = circle('moden',5)
print(kodo.ara())