class Family:
    def __init__(self, address) -> None:
        self.address = address

class School:
    def __init__(self, id, level) -> None:
        self.id = id
        self.level = level

class Sports:
    def __init__(self, game) -> None:
        self.game = game

class Student(Family, School, Sports):
    def __init__(self, address, id, level, game) -> None:
        Family.__init__(self, address)
        School.__init__(self, id, level)
        Sports.__init__(self, game)
        
    def __repr__(self) -> str:
        return super().__repr__()

s = Student('pathkhat', 20, 1, 'free fair')
print(s.address,s.game,s.id,s.level)
