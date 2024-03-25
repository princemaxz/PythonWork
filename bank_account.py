class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, initialAmount, AccoutName):
        self.balance = initialAmount
        self.name = AccoutName
        print(f"\nAccount '{self.name}', created.\nBalance = ${self.balance:.2f}")
        # print(f"\nAccount '{self.name}', created.\nBalance = ${self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\nDeposit complete.")
        self.getBalance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, Account '{self.name}' only has a balance of ${self.balance:.2f}"
            )

    def Withdrawal(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdrawal Complete.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdrawal Interupted: {error}")

    def transfer(self, amount, account):
        try:
            print("\n********** \n\n Begining Transfer....🚀")
            self.viableTransaction(amount)
            self.Withdrawal(amount)
            account.deposit(amount)
            print("\nTransaction Complete! ✅\n\n**********")

        except BalanceException as error:
            print(f"\nTransfer Interupted. ❌ {error}")


class InterestRewardAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit Complte.")
        self.getBalance()


class SavingsAcct(InterestRewardAcct):
    def __init__(self, initialAmount, AccoutName):
        super().__init__(initialAmount, AccoutName)
        self.fee = 5

    def Withdrawal(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdrawal Complete.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdrawl Interupted {error}")
