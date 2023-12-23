class person:
    def __init__(self,name,age,hight,weight) -> None:
        self.name = name
        self.age = age
        self.hight = hight
        self.weight = weight
    def eat(self):
        print("alo kodo and another energy")
    def exercise(self):
        raise NotImplementedError
class crickter(person):
    def __init__(self, name, age, hight, weight,team) -> None:
        self.team = team
        super().__init__(name, age, hight, weight)

    def eat(self): # overriting
        print("eating vesitablae only")
    def exercise(self):
        print("every day must be workout")
    def __add__(self,other):
        return self.age + other.age
    def __mul__(self,other):
        return self.weight * other.weight
    def __len__(self):
        return self.hight
    def __gt__(self,other):
        return self.age > other.age
    
korinm = crickter("moden",40,53,63,"bd")
mosi = crickter("mosi",63,56,40,"lk")

# korinm.eat()
# korinm.exercise()
print(45+ 3)
print("sakib" + "rana")
print([12,69] + [5,6,5])
print (korinm + mosi)
print(korinm * mosi)
print(len(korinm))
print(korinm > mosi)