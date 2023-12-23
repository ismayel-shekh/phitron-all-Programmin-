# global variable
balance = 3000
def buy_thing(item, price):
    #local scope variable 
    # you can access global variable without USING  the gloval balence
    global balance
    print(f'previous balance value', balance)
    balance = balance-price
    print(f'balance after bying {item}', balance)
buy_thing('sungless',1000)
print('global balance after boy ',balance)
