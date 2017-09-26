

# Banking System

class BankingSystem:

    def __init__(self, name, age, email, balance = 0, acct = None):
        self.age = age
        self.name = name
        self.email = email
        self.balance = balance
        self.acct = acct

    def balance(self):
        return self.balance

    def deposit(self, money):
        if money:
            self.balance += money
        return self.balance


    def withraw_funds(self, money):
        if self.balance > 0:
            self.balance -= money
        else:
            print("Not enough money")
        return self.balance

Raj = BankingSystem("Raja Shekar", 27, "r@gmail.com", 500)

print Raj.balance

Raj.deposit(500)

print Raj.balance

Raj.withraw_funds(100)

print Raj.balance
