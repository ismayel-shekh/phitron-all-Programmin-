from abc import ABC,abstractclassmethod
class shape(ABC):
    @abstractclassmethod
    def area(self):
        pass
    @abstractclassmethod
    def perimeter(self):
        pass
class square(shape):
    def __init__(self,side) -> None:
        shape.__side = side
    def area(self):
        return self.__side * self.__side
    def perimeter(self):
        return 4 * self.__side
    # def alo(self):
    #     print("king is back ")
square = square(5)
print(square.area())
print(square.perimeter())