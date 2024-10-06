# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the account with an optional starting balance."""
        self.__account_balance = initial_balance  # Encapsulated attribute
    
    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        self.__account_balance += amount
    
    def withdraw(self, amount):
        """Withdraw an amount if sufficient funds are available."""
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Print the current account balance."""
        print(f"Current Balance: ${self.__account_balance:.2f}")

