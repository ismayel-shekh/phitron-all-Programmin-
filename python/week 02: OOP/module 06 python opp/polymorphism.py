# poly --> many (multiple)
# morph --> ahape

class animal:
    def __init__(self,name) -> None:
        self.name = name
    def marke_sound(self):
        print('animal making same sound')
class cat(animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def marke_sound(self):
        print('meow meow')
class Dog(animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def marke_sound(self):
        print('gheu gheu')
class goat(animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def marke_sound(self):
        # return super().marke_sound() # that line provided output animal making same sound
        print('beh beh beh')
don = cat('real don')
don.marke_sound()

shepard = Dog('local shephard')
shepard.marke_sound()

mess = goat('L,M')
mess.marke_sound()

less = goat('bora gori')
animals =[don,shepard,mess,less]
for animal in animals:
    animal.marke_sound()

