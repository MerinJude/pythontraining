#OOP modelling of a bank account as class and objects
class BankAccount:
    def __init__(self): #initializes an instance of bankaccount by naming it as self
        self.balance = 0

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance
a = BankAccount()
b = BankAccount()
a.deposit(100)
print(a.balance)
print(b.balance)
#inheritance
class MinimumBalanceAccount(BankAccount): #inherits bank account class
    def __init__(self, minimum_balance):
        BankAccount.__init__(self) #initalises as per class bank account
        self.minimum_balance = minimum_balance #sets min balance criteria

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance: #if it fails min bal criteria
            print('Sorry, minimum balance must be maintained.')
        else:
            BankAccount.withdraw(self, amount) #otherwise successful withdrawal
c=MinimumBalanceAccount(500)
c.deposit(1000)
c.withdraw(400)
print(c.balance)
c.withdraw(150)
print(c.balance)

