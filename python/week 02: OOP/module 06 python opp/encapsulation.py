# encapsulation --> hide details
# access modifier : public,proteced,privete
class bank:
    def __init__(self,holder_name,initial_deposit) -> None:
        self.holder_name = holder_name #public attribute
        self._branch = 'banani 11'# protected
        self.__balance = initial_deposit #private
    
    def deposit(self,amount):
        self.__balance += amount
    def get_balance(self):
        return self.__balance
    
    def withdrow(self,amount):
        if amount <self.__balance:
            self.__balance -= amount
            return amount
        else:
            return f'fokira taka nhi'
rufsan = bank('chooto bro',10000)
print(rufsan.holder_name)
print(rufsan._bank__balance)
rufsan.holder_name = 'boro vai'
rufsan.deposit(40000)
print(rufsan.get_balance())
print(rufsan.holder_name)
print(rufsan._branch)
# print(dir(rufsan))
print(rufsan._bank__balance)