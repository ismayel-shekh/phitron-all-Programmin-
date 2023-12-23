class bank:
    def __init__(self,balance):
         self.balance = balance
         self.min_balance = 100
         self.max_balance = 20000
    
    def check_balance(self):
        return self.balance
    
    def deposit(self,amount):
        if amount >= self.min_balance and amount <= self.max_balance:
            self.balance += amount
        else: print("Try again! You should to deposite 100 to 20000")
    
    def withdraw(self,amount):
        if self.balance < self.min_balance:
            print("Your account Balance {self.balance}\nFor withdrw your balance have minmum 100")
        elif amount < 100:
            print("Try again! Your diposit amount is less then 100")
        elif amount > self.max_balance:
            print("Try again! Your amount is range over")
        else:
            self.balance -= amount
    
Bank_asia = bank(0)
N = input("Select any option:\n 1.Account balance chack\n 2.Deposit Money \n 3.Withdraw Money\n 4.Sent money\nEnter a number: ")

if (N >= 1 and N <= 4):
    if N == 1:
        print(Bank_asia.check_balance())
    elif N == 2:
        deposit_money = input("Enter deposit amount: ")
        Bank_asia.deposit(deposit_money)
        print("Current balance: ", Bank_asia.check_balance())
    elif N == 3:
        withdraw_money = input("Enter withdraw amount: ")
        Bank_asia.withdraw(withdraw_money)
        print("Current balance : {Bank_asia.check_balance()}")
else:
    print("Try again! You are dial a wrong number")

