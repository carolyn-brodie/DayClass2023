from BankAccount import *

account1 = BankAccount(123, "JimBob")
account2 = BankAccount(456, "Jane")
account2 = account1

account1.deposit(100)
print("account1:", account1)
print("account2:", account2)