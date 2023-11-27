class Account:
    def __init__(self, account_nr, balance=0):
        self.account_number =account_nr
        self.balance = balance
    
    def deposit(self,amount):
        self.balance += amount
        print(f"Amount = ${amount}. Cuurent balance = ${balance}\n")
    
    def withdrawal(self, amount):
        if(self.balance >= amount):
            self.balance -= amount
            print(f"Amount = ${amount}. Cuurent balance = ${balance}\n")
        else: print("Insufficient funds.")
    
class SavingsAccount(Account):
    def __init(self, account_nr, balance=0, interest_rate=0.01):
        Account.__init__(account_nr. balance)
        self.interest_rate = interest_rate

    def calc_interest(self):
        interest = self.interest_rate * self.balance
        self.deposit(interest)
        print(f"Interest addedL {interest}")



