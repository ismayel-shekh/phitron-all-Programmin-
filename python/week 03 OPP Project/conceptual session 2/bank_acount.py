from abc import ABC,abstractmethod

class Account(ABC):
    account = []
    def __init__(self,name,accNumber,password,type) -> None:
        self.name = name
        self.accNo = accNumber
        self.passw = password
        self.type = type
        self.balance = 0

        Account.account.append(self)
    def deposit(self,amount):
        if amount >=0:
            self.balance += amount
        else:
            print("\n Invalid amount\n")
    def withdraw(self,amount):
        if amount >= 0 and amount <= self.balance:
            self.balance -= amount
        else:
            print('\n Invalid amount')
    def changeInfo(self,name):
        self.name = name
    #over loading of mathod changeInfo
    def changeInfo(self,name,passoword):
        self.name = name
        self.passw = passoword 
    @abstractmethod
    def showInfo(self):
        pass
class SavingsAccount(Account):
    def __init__(self,name,accNumber,password,interestrate):
        super().__init__(name,accNumber,password,"savings")
        self.iRate = interestrate
    def showInfo(self):
        print(f'Infos of account {self.name}\n')
        print(f'\n Account Noumber: {self.accNo}')
        print(f'\n Account Type: {self.type}\n')
        print(f'\n Balance: {self.balance}')
    def applyInterest(self):
        interest = self.balance * (self.iRate/100)
        print(f'\nApplied interest of {interest}')
        self.deposit(interest)
class SpecialAccount(Account):
    def __init__(self, name, accNumber, password, limit) -> None:
        super().__init__(name, accNumber, password, "special")
        self.limit = limit
    def  withdraw(self, amount):
        if amount >= 0 and amount <= self.limit:
            self.balance -= amount
        else:
            print('\n Invalid amount')
    def showInfo(self):
        print(f'\nInfos of {self.type} account {self.name}\n')
        print(f'Account Number: {self.accNo}')
        print(f'\nBalance: {self.balance}')
currentuser = None
while(True):
    if currentuser == None:
        print('\n Loing User Logged in !\n')
        ch = input('\n Login or Register(L/R)')
        if ch == "R":
            name = input("name: ")
            nu = input("account Number: ")
            pa = input("password: ")
            a = input("savings or special? (sv/sp)")
            if a=="sv":
                irate = int(input("Interast rate: "))
                currentuser = SavingsAccount(name,nu,pa,irate)
            elif a=="sp":
                lim = int(input("overdraft rate: "))
                currentuser = SpecialAccount(name,nu,pa,lim)
            else:
                print("\nInvalid Choice\n")   
        else:
            nu = input("account Number: ")
            for account in Account.accounts:
                if nu == account.accNo:
                    currentuser = account
                    break
    else:
        print("\n Wellcome {currentuser.name}! \n")
        if currentuser.type == "savings":
            print("1. Show info")
            print("2. Deposit")
            print("3. withdraw")
            print("4. Apply Interest")
            print("5. Change Info")
            print("6. Logout")

            op = int(input("Choose Option: "))
            if op == 1:
                currentuser.showInfo()
            elif op == 2:
                am = int(input("amount: "))
                currentuser.deposit(am)
            elif op == 3:
                am = int(input("amount: "))
                currentuser.withdraw(am)
            elif op == 4:
                currentuser.applyInterest()
            elif op == 5:
                #todo
                pass
            elif op == 6:
                currentuser = None
        else:
            print("1. show info")
            print("2. Deposit")
            print("3. withdraw")
            print("4. chage Info")
            print("5. Logout")
            op = int(input("Chose option: "))
            if op == 1:
                currentuser.showInfo()
            elif op == 2:
                am = int(input("amount: "))
                currentuser.deposit(am)
            elif op == 3:
                am = int(input("amount: "))
                currentuser.withdraw(am)
            elif op == 4:
                #topd o
                print("home work")
            elif op == 5:
                currentuser = None
            
            
