class pan:
    def __init__(self,brand,name,colors) -> None:
        self.brand = brand
        self.name = name
        self.colors = colors
    def pan_detels(self):
        print("pan name : " + self.name +"\npan company : " + self.brand + "\npan colors : " + self.colors)
print("if you start program pass 0 or 1")
x = int(input())
if x == 0 :
    p = pan(input("give brand : "),input("give pan name: "),input("whies colors : "))
    p.pan_detels()
elif x == 1:
    print("sestem far dnanga")
else:
    print("dur bot bul number das")