"""
Banking System Implementation in Python
This program demonstrates the use of all 33 Python keywords.
"""

# Import required modules (for demonstration)
import random

# Define a BankAccount class to manage accounts
class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = balance
        self.transactions = []
    
    def deposit(self, amount: float):
        assert amount > 0, "Deposit amount must be positive"
        self.balance += amount
        self.transactions.append(("deposit", amount))
        return self.balance
    
    def withdraw(self, amount: float):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self.transactions.append(("withdraw", amount))
        return self.balance
    
    def history(self):
        for transaction in self.transactions:
            print(transaction)

# Global dictionary to store bank accounts
global accounts
accounts = {}

def create_account(name):
    global accounts
    if name in accounts:
        print("Account already exists!")
        return None
    accounts[name] = BankAccount(name)
    return accounts[name]

def special_function():
    value = 10
    def inner():
        nonlocal value
        value += 5
        return value
    return inner()

def lambda_demo(x):
    return (lambda y: y * 2)(x)

def risky_operation():
    try:
        num = random.choice([0, 1])
        if num == 0:
            raise ZeroDivisionError("Simulated error")
    except ZeroDivisionError as e:
        print("Caught exception:", e)
    finally:
        print("Finally block executed")

def main():
    print("Welcome to the Python Bank System!")
    while True:
        print("\nOptions: create, deposit, withdraw, history, exit")
        choice = input("Enter your choice: ")
        
        if choice == "exit":
            break
        elif choice == "create":
            name = input("Enter your name: ")
            create_account(name)
            print("Account created successfully!")
        elif choice in ("deposit", "withdraw", "history"):
            name = input("Enter account name: ")
            if name not in accounts:
                print("Account does not exist!")
                continue
            if choice == "history":
                accounts[name].history()
            else:
                amount = float(input("Enter amount: "))
                if choice == "deposit":
                    accounts[name].deposit(amount)
                    print("Deposited successfully! New balance:", accounts[name].balance)
                else:
                    try:
                        accounts[name].withdraw(amount)
                        print("Withdrawn successfully! New balance:", accounts[name].balance)
                    except ValueError as e:
                        print(e)
        else:
            print("Invalid choice. Try again.")
        
        # Demonstrate use of pass
        if False:
            pass
        
        # Demonstrate use of with
        with open("log.txt", "w") as file:
            file.write("Transaction Log\n")
        
        # Demonstrate yield
        def generator():
            yield "Generated Value"
        print(next(generator()))

if __name__ == "__main__":
    main()
