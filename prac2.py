class Account:
    def __init__(self,number):
        self.number = number
        self.amount = 0
    def get_balance(self):
        return self.amount
    def deposit(self,amt):
        self.amount+=amt
    def withdraw(self,amt):
        if self.amount>=amt:
            self.amount-=amt
        else:
            print("Amount is less")
def transfer_amount(acc_1,acc_2,amount):
    acc_1.withdraw(amount)
    acc_2.deposit(amount)
ac1 = Account("001")
ac2 = Account("002")
ac1.deposit(500)
ac2.deposit(1000)
ac2.withdraw(250)
transfer_amount(ac2,ac1,250)
print(ac1.get_balance())
print(ac2.get_balance())
    