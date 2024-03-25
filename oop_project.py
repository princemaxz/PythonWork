from bank_account import *

Prince = BankAccount(1000, "Prince")
Jojo = BankAccount(1500, "Jojo")


Prince.getBalance()
Jojo.getBalance()


Jojo.deposit(20000)

Prince.Withdrawal(5000)
Prince.Withdrawal(200)

print("\n\n")

Prince.transfer(2000, Jojo)
print("\n")

Prince.transfer(200, Jojo)

print("\n")

Keli = InterestRewardAcct(1000, "Keli")
Keli.getBalance()
Keli.deposit(100)
Keli.transfer(100, Prince)

print("\n")

Maxz = SavingsAcct(2000, "Maxz")
Maxz.getBalance()
Maxz.deposit(100)
Maxz.transfer(200000, Jojo)
Maxz.transfer(200, Jojo)
print("\n\n\n")
