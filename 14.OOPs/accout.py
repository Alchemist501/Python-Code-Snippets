import random


class account:
    balance = 2000

    def __init__(self):
        self.accountNo = "PY24".__add__(str(random.randint(100, 1000)))
        print("Account number is :", self.accountNo)

    def debit(self, amnt):
        if self.balance > 2000:
            self.balance -= amnt
            print(amnt, "debited from your account")
        else:
            print("Minimum balance is 2000 INR")

    def credit(self, amnt):
        self.balance += amnt
        print(amnt, "credited to your account")

    def printBalance(self):
        print("Balance is : ", self.balance)


me = account()
me.printBalance()
me.debit(200)
me.credit(5000)
me.printBalance()
me.debit(2000)
me.printBalance()
