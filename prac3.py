class Bank:
    bal = 0
    def __init__(self,account_number):
        self.account_number = account_number
        self.amount = 0
    @classmethod
    def message(cls,am):
        cls.bal = am
        print(f"Balance in the account is:{Bank.bal}")
    def deposit(self,amt):
        self.amount+=amt
        am = self.amount
        Bank.message(am)
a = Bank("001")
a.deposit(1000)
b = Bank("002")
print(Bank.bal)

