class BankAccount:
            def __init__(self, int_rate=0.04, balance=0):
                self.intrate = int_rate
                self.bal=balance
                

            def deposit(self, amount):
                self.bal+=amount
                return self

            
            def withdraw(self, amount):
                self.bal-=amount
                return self
                
            def display_account_info(self):
                print(self.bal , self.intrate)
                return self
                
            def yield_interest(self):
                self.yieldIntr=self.bal*self.intrate
                return self


account1=BankAccount()
account2=BankAccount()

account1.deposit(1000).deposit(200).deposit(140).withdraw(150).yield_interest().display_account_info()
account2.deposit(400).deposit(200).withdraw(100).withdraw(120).withdraw(50).yield_interest().display_account_info()


		
