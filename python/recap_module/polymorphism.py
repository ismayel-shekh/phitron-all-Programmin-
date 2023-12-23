class animal:
    def __init__(self,name) -> None:
        self.name = name
    def make_sound(self):
        print("hello king ")
class cat(animal):
    def __init__(self, name) -> None:
        super().__init__(name)
class dog(animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def make_sound(self):
        print("gaw gaw")

bili = cat("bili")
bili.make_sound()
bulo  = dog("bulo")
bulo.make_sound()