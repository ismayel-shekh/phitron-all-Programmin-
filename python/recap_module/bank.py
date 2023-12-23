class bank:
    def __init__(self,holder_name,initial_deposit) -> None:
        self.holder_name = holder_name
        self._brance = "mirpur 11 "
        self.__balance = initial_deposit
    def deposit(self,amount):
        self.__balance += amount
    def get_balance(self):
        return self.__balance
    def withdrow(self,amount):
        if amount < self.__balance:
            self.__balance -= amount
        else:
            return f"bank a taka nhi"
    __balance = 50000
dpl = bank("ismayel",10000)
print(dpl.get_balance())
dpl.__balance = 400000
print(dpl._bank__balance)