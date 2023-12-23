class user:
    def __init__(self,name,age,money) -> None:
        self._name = name
        self._age = age
        self.__money = money
    @property
    def age(self):
        return self._age
    @property
    def salary(self):
        return self.__money
    @salary.setter
    def salary(self,value):
        if value < 0:
            print("salary value not be negative")
        else:
            self.__money += value
        return self.__money
samsu = user("kopa",21,20000)
# print(samsu.__money)
# print(samsu.age())
print(samsu.age)
print(samsu.salary)
samsu.salary = 4500
print(samsu.salary)
# # print(samsu.__money)
# # print(samsu.age()) 
# print(samsu.age)
# print(samsu.salary)
# samsu.salary = 4500
# print(samsu.salary)