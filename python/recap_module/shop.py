class Shop:
    shoping_moll = input()
    all_card= []
    def __init__(self,bayer_name,qunatity) -> None:
        self.bayer_name = bayer_name
        self.qunatity = qunatity
        self.card = []
    def add_to_card(self,item):
        self.card.append(item)
sakil = Shop("sakils",7)
sakil.add_to_card("alo")
print(*sakil.card)
shohid = Shop("king ",80)
shohid.add_to_card("kod0")
print(*shohid.card)