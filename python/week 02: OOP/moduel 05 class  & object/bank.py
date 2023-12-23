class bank:
    def __init__ (self,balance):
        self.balance = balance
        self.min_withdrow =100
        self.max_withdrow = 1000000
    def get_balance(self):
        return self.balance
    def deposit(self,amount):
        if amount >0:
            self.balance+=amount
            
    def withdrow(self,amount):
        if amount < self.min_withdrow :
            print(f'you blady gorivb lok not with drow it{self.min_withdrow}')
        elif amount > self.max_withdrow:
            print(f'bhi map koira dan bank gorib hoia jaiba{self.max_withdrow}')
        else:
            self.balance -= amount
            print(f'here is your money {amount}')
            print(f'your balance after withdrow{self.balance}')
fcb = bank(20000)
fcb.withdrow(25)
fcb.withdrow(400000000)
fcb.withdrow(10000)

blc = bank(30000)
blc.deposit(2000)
blc.deposit(40000)
print(blc.get_balance())

