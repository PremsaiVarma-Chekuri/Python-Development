# Bank Application

class Bank:
    def __init__(self,account_number):
        self.account_number = account_number
        self.balance = 0
    def get_balance(self):
        return self.balance
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
        else:   
            print("Insufficient balance")
    def deposit(self,amount):
        self.balance+=amount

def transfer_amount(acc_1,acc_2,amount):
    acc_1.withdraw(amount)
    acc_2.deposit(amount)

user_1 = Bank("001")
user_2 = Bank("002")
user_1.deposit(500)
user_2.deposit(1000)
print("User 1 Balance: {}/-".format(user_1.get_balance()))
print("User 2 Balance: {}/-".format(user_2.get_balance()))
transfer_amount(user_1, user_2, 50)
print("Transferring 50/- from User 1 to User 2")
print("User 1 Balance: {}/-".format(user_1.get_balance()))
print("User 2 Balance: {}/-".format(user_2.get_balance()))

