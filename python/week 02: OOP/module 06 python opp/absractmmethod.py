from abc import ABC, abstractmethod
# absreact base class
class Animal(ABC):
    @abstractmethod #enforce all devived class to have a eat method
    def eat(self):
        print('I need food')

    @abstractmethod
    def move(self):
        pass
class monkey(Animal):
    def __init__(self,name) -> None:
        self.category ='monkey'
        self.name = name
        super().__init__()
    def eat(self):
        print('hay na nana, I am eating banana')
    
    def move(self):
        print('hanging on the pranches')
    
layka = monkey('lucky')
layka.eat()
