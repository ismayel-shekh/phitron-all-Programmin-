class person:
    def __init__(self,name,age,height,weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    def eat(self):
        print('vat mangso polau korma')

    def exercise(self):
        raise NotADirectoryError

class cricketer(person):
    def __init__(self, name, age, height, weight,team) -> None:
        self.team = team
        super().__init__(name, age, height, weight)

    def eat(self):
        print('vagetable')
    def exercise(self):
        print('gym e poisa diya hudai gham jorai')
    
    def __add__(self,other):
        return self.age + other.age
    
    def __mul__ (self, other):
        return self.weight * other.weight
    def __len__(self):
        return self.height
    def __gt__(self, other):
        return self.age > other.age
    
sakib = cricketer('sakib',38,68,91,'BD')
# sakib.eat()
# sakib.exercise()
mushi = cricketer('mushi',36,65,78,'BD')
print('sakib' + 'mushi')
print([12, 98] + [5, 6, 7, 1, 2])
print(sakib+mushi)
print(sakib*mushi)
print(len(sakib))
print(sakib > mushi)