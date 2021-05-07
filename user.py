class User: 

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def printRunningTotal(self):
        print(f"{self.name} has {self.account_balance} amount in the bank")
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        print(f"{self.name} took out {amount} from the bank acount")
        self.printRunningTotal()
        return self

    def make_deposit(self, amount):
        self.account_balance += amount
        print(f"{self.name} deposited {amount} in bank acount")
        self.printRunningTotal()
        return self

    def transfer_money(self, User, amount):
        print(f" transfer from {self.name} to {User.name} with an amount {amount}")
        self.make_withdrawal(amount)
        User.make_deposit(amount)
        return self


guido = User("Guido van Rossum", "guido@python.com") 
monty = User("Monty Python", "monty@python.com") 
elmo = User("Elmo", "elmo@sesemestreet.com")

print(guido.name) 
print(monty.name)


guido.make_deposit(1000)

monty.make_deposit(10)


print(guido.account_balance)

print(monty.account_balance)

guido.transfer_money(monty, 50)

print(guido.account_balance)

print(monty.account_balance)

