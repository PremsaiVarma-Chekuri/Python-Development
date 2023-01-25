class Bank:
    def __init__(self,name,acccount_number):
        self.name = name
        self.account_number = acccount_number
        self.balance = 0
class Pnb(Bank):
    def return_balance(self,amt):
        print(f"Balance in Pnb is : {amt}")
    def credit(self,amount):
        self.balance+=amount
        #self.return_balance(self.balance)
    def debit(self,amount):
        if self.balance<amount:
            print("Insufficient balance")
        else:
            self.balance-=amount
            #self.return_balance(self.balance)

class Sbi(Bank):
    def return_balance(self,amt):
        print(f"Balance in Pnb is : {amt}")
    def credit(self,amount):
        self.balance+=amount
        #self.return_balance(self.balance)
    def debit(self,amount):
        if self.balance<amount:
            print("Insufficient balance")
        else:
            self.balance-=amount
            #self.return_balance(self.balance)
def tranfer(acc1,acc2,amt):
    acc1.debit(amt)
    acc2.credit(amt)
    print(f"The balance in PNB is:{acc1.balance}")
    print(f"The balance in SBI is:{acc2.balance}")


first_bank = Pnb("Premsai Varma","001")
first_bank.credit(1000)

second_bank = Sbi("Premsai Varma","002")
second_bank.credit(2000)

tranfer(first_bank,second_bank,500)
tranfer(second_bank,first_bank,500)

    