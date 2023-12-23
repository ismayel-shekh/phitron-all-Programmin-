class animal:
    def __init__(self,name) -> None:
        self.name = name
    def eat(self):
        print(self.name,"I can eat")
class cat(animal):
    def __init__(self, name) -> None:
        animal.__init__(self,name)
    def speak(self):
        print("I can eat")
class dog(animal):
    def speak(self):
        print("i can hell0")
c = cat('cat')
c.eat()
c.speak()
d = dog("dog")
d.eat()
d.speak()