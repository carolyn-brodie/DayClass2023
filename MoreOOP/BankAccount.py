## Bank Account Class

class BankAccount(object):
    """Models a simple bank account"""

    ##Constructor
    def __init__(self, aNumber, owner):
        self.owner = owner
        self.accountNum = aNumber
        self.balance = 0


    ##Other methods
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")
         
    def getBalance(self):
        return self.balance
     
    ##Print method
    def __str__(self):
        out = self.owner + " has account nunber " + str(self.accountNum)
        out = out + " with balance " + str(self.balance)
        return out


     

def testBankAccount():
     print("Test BankAccount class")
     acct = BankAccount(123,"Joe Account")
     print(acct)

if __name__ == "__main__":
    testBankAccount()
    
