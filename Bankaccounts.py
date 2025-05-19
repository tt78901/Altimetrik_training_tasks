# Base Class: BankAccount
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")
        else:
            print("Insufficient funds or invalid amount.")
    
    def get_balance(self):
        return self.balance
    
    def display_account_info(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")

# Subclass: SavingsAccount
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate
    
    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest applied: {interest}. New balance: {self.balance}")

# Subclass: CheckingAccount
class CheckingAccount(BankAccount):
    def __init__(self, account_holder, balance=0, overdraft_limit=500):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        if amount > 0 and (self.balance + self.overdraft_limit) >= amount:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")
        else:
            print("Withdrawal exceeds overdraft limit.")

# Testing the classes
if __name__ == "__main__":
    # Creating a savings account
    savings = SavingsAccount("Alice", 1000)
    savings.display_account_info()
    savings.deposit(500)
    savings.apply_interest()

    print("\n---\n")
    
    # Creating a checking account
    checking = CheckingAccount("Bob", 200, 300)
    checking.display_account_info()
    checking.withdraw(450)  # This should work due to the overdraft
    checking.withdraw(1000)  # This should fail as it exceeds the overdraft

