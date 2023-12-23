class sports:
    def __init__(self,game) -> None:
        self.game = game
    def __repr__(self) -> str:
        return f"king is back"
class school:
    def __init__(self,name) -> None:
        self.name = name
    def __repr__(self) -> str:
        return f"hello brothor"
class student(sports,school):
    def __init__(self, game,name) -> None:
        sports.__init__(self,game)
        school.__init__(self,name)
    def __repr__(self) -> str:
        return school.__repr__(self)
    # def __repr__(self) -> str:
    #     return super().__repr__()
satro = student( "hoky","moden")
print(satro)