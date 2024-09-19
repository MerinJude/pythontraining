#modelling a bank account with dictionary
def make_account():
    return {'balance': 0}

def deposit(account, amount):
    account['balance'] += amount
    return account['balance']

def withdraw(account, amount):
    account['balance'] -= amount
    return account['balance']
a = make_account() #makes a dict for a with key "balance"
b = make_account() #makes a dict for b with key "balance"
print(deposit(a, 100))
print(deposit(b, 100))
print(deposit(b, 100))
print(withdraw(a, 20))
