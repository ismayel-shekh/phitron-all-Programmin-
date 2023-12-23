class engine:
    def __init__(self,name) -> None:
        self.name= name
    def sr(self):
        print(f"{self.name} start te car")
class driver:
    def __repr__(self,name) -> str:
        self.name = name
        print(f"{self.name} drive that car")
class car:
    def __init__(self,name) -> None:
        self.name = name
        self.engine = engine(name)
        self.driver = driver()
    def start(self):
        self.engine.sr()
gari = car("heillo")
gari.start()