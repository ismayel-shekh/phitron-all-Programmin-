class grandfather:
    def __init__(self) -> None:
        pass
    def property(self):
        print("I have 5 corer taka")
class father(grandfather):
    def property(self):
        print("I have 3 corer taka")
    def father_property(self):
        super().property()
class child(father):
    def property(self):
        print("I have 1 corer taka")
    def father_property(self):
        super().property()
    def grandfather_property(self):
        super().father_property()

ami = child()
ami.property()
ami.father_property()
ami.grandfather_property()