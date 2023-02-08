class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, money):
        self.balance += money
        print('New balance: {}'.format(self.balance))
    def withdraw(self, money):
        if self.balance < money or money < 0:
            return print("not enough money")
        self.balance -= money
        print('New balance: {}'.format(self.balance))
    
test = Account("Sergey", 1000)
test.withdraw(1000)
test.deposit(2000)
test.withdraw(2001)
test.withdraw(-1000)
test.deposit(1000000)
test.withdraw(2000)
            
