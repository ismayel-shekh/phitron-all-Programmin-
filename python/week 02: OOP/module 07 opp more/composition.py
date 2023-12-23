class Enging:
    def __init__(self) -> None:
        # self.mobil = mobil
        # print("hello bro")
        pass
    def start(self):
        return "engnine srarted"
class Driver:
    def __init__(self) -> None:
        pass
class car:
    def __init__(self) -> None:
        self.enging = Enging()
        self.driver = Driver()
    
    def start(self):
        self.enging.start()
x = car()
# print(x.driver)
# x.enging(40)
# print(x.enging.mobil)