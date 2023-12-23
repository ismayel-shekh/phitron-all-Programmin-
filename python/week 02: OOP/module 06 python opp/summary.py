class Book:
    def __init__(self,name) -> None:
        self.name = name
    def read (self):
        raise NotImplementedError # that is an error
class physics(Book):
    def __init__(self, name,lab) -> None:
        self.lab = lab
        super().__init__(name)
    def read(self):
        print('rading vector')
topon = physics('topon',True)
print(issubclass(physics,Book))
print(isinstance(topon,physics))
print(isinstance(topon,Book))
topon.read()