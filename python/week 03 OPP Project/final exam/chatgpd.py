import random
class Bank:
    def __init__(self) -> None:
        self.users = []
        self.admin = None
        self.bank_balance = 10000
        self.loan_feature = True
    def create_user_account(self,name,email,address,account_type):
        if not self.loan_feature:
            print(f'Bank is not currently offering loans')
        user = User(name,email,address,account_type)
        self.users.append(user)
        print('succesfully creating account!!')

    def delete_user_acount(self,user):
        self.users.remove(user)
    def all_user_account(self):
        for usre in self.users:
            print(usre)
    def available_balance(self):
        amount = sum(User.blance for usr in self.users)
        print(f'total available amount {amount}')

    def total_loan_amount(self):
        loan = sum(user.loan_taken for user in self.users)
        print(f'Total loans {loan} taka')

    def loan_taken_feature(self):
        self.loan_feature = not self.loan_feature


class User:
    def __init__(self,name,email,address,type) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.type = type
        self.account_number = None
        self.balance = 0
        self.loan_taken = 0
        self.create_account_number()
        self.transction_history = []
    
    def create_account_number(self):
        number = random.randint(1000,9999)
        print('your account number is',number)
        self.account_number = number
    def deposit(self,amount):
        if amount >= 0:
            self.balance += amount
            print(f"succesfully deposit {amount} taka")
            self.transction_history.append(f'deposit {amount} taka\n')
        else:
            print('Invalid')
    def withdrow(self,amount):
        if amount >= 0 and amount <= self.balance:
            self.balance -= amount
            print('succesfully withdrow now your balance is ',self.balance)
            self.transction_history.append(f'withdrow {amount} taka\n')
        else:
            print('Withdrawal amount exceeded!!!!')
    def available_balance(self):
        print(f'Available balance {self.balance}')

    def take_loan(self,amount):
        if self.loan_taken < 2:
            self.loan_taken += 1
            self.balance += amount
            print(f'succesfully taken loan {amount} taka')
            self.transction_history.append(f'Take a loan of {amount} taka\n')
        else:
            print(f'You have reached the maximum number of loans!!!!!!!')

    def transfer_balance(self,amount,transfer_account):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            # transfer_account.balance += amount
            print(f'succesfully transfer {amount} taka')
            self.transction_history.append(f'transfer {amount} taka {transfer_account} account!!\n')
        else:
            print('Account does not exist')

print('----------------wellcome to PYthon bank ---------------')
current_user = None
python = Bank()
while True:
    if current_user is None:
        print('---------no user logged in !----------\n')
        print(" 1. create account \n 2. exit" )
        ch = int(input('Enter option: '))
        if ch == 1:
            na = input("name :")
            em = input('email :')
            ad = input('address : ')
            typ = input('type :')
            current_user = User(na,em,ad,typ)
            if current_user.name == 'admin':
                print('---------------wellcome to admin panal-------------')
                print("1. create acount.\n2. delete user account.\n3. see all user accounts.\n4. bank available balance.\n5. total loan amount.\n6. on or off loan feature.\n")
            else:
                print('\n\n-----------------wellcome to python bank-----------\n')
                while True:
                    print(
                        '\n\n\n'
                        '1. sow account number.\n'
                        '2. deposit.\n'
                        '3. withdrow.\n'
                        '4. avalilable balance.\n'
                        '5. transaction history.\n'
                        '6. loan taken.\n'
                        '7. transfer amount.\n'
                        '8. exit.\n'
                    )
                    op = int(input('Enter option: '))
                    if op == 1:
                        current_user.create_account_number()
                        break
                    elif op == 2:
                        am = int(input('amount : '))
                        current_user.deposit(am)
                    elif op == 3:
                        wi = int(input('amount : '))
                        current_user.withdrow(wi)
                    elif op == 4:
                        current_user.available_balance()
                    elif op == 5:
                        print(*current_user.transction_history)
                    elif op == 6:
                        am = int(input('amount: '))
                        current_user.take_loan(am)
                    elif op == 7:
                        tf = input('transfar account number: ')
                        am = int(input('amount: '))
                        current_user.transfer_balance(am,tf)
                    elif op == 8:
                        current_user = None
                        break
                    else:
                        print("please pass currect number!!")
        elif ch == 2:
            break


if ch == 1:
            name = input("user name : ")
            pas = input("password : ")
            current_user = python.find_acount(name,pas)
            if current_user != None:
                print('\n\n-----------------welcome to Python bank-----------\n')
                while True:
                    print('\n\n\n'
                    '1. Show account number\n'