class user:
    def __init__(self,name,age,email,n1,n2):
        self.name=name
        self.email=email
        self.age=age
        self.balance=[BankAccount(n1,n2)]
    def newbankaccount(self,n1,n2):
        self.balance.append(BankAccount(n1,n2))
    def withdraw(self,amount,banknum):
        self.balance[banknum].withdraw(amount)
    def deposit(self,amount,banknum):
        self.balance[banknum].deposit(amount)
class BankAccount:
    def __init__(self,rate,balance):
        self.balance=balance
        self.rate=rate
    def deposit(self,amount):
        self.balance+=amount
        return self
    def withdraw(self,amount):
        self.balance-=amount
        return self
    def display(self):
        return self.balance
    def yield_interest(self):
        self.balance=self.balance+(self.rate*self.balance)
        return self
rain=user("rain",27,"r@gmail.com",20,20)
print(rain.balance[0].display())