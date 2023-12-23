class Company:
    def __init__(self,name ,address) -> None:
        self.name = name
        self.address =address
        self.bus = []
        self.routes = []
        self.drivers =[]
        self.counter=[]
        self.manager =[]
        self.supervisors =[]
        self.fare = []
class Driver:
    def __init__(self,name,license,age) -> None:
        self.license = license
        self.name = name
        self.age = age
        self.driver = []
    def add_to_driver(self,name,licence,age):
        item = f'name: {name},licence : {licence},age: {age}'
        self.driver.append(item)
class bus:
    def __init__(self,name,number) -> None:
        self.name =name
        self.number = number
        self.bus = []
    def add_bus(self,name,number):
        item=f'name: {name},number: {number}'
        self.bus.append(item)
ali = ('ali',20,40)
print(Driver.driver)