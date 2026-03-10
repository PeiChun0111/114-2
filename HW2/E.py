class NegativeAmountError(Exception):
    pass
class InsufficientFundsError(Exception):
    pass
class BankAccount:
    def __init__(self):
        self.balance = 0
    def deposit(self, amount):
        if amount < 0:
            raise NegativeAmountError
        self.balance += amount
    def withdraw(self, amount):
        if amount < 0:
            raise NegativeAmountError
        if amount > self.balance:
            raise InsufficientFundsError
        self.balance -= amount
n = int(input())
account = BankAccount()
for _ in range(n):
    cmd, amt = input().split()
    amt = int(amt)
    try:
        if cmd == "D":
            account.deposit(amt)
        elif cmd == "W":
            account.withdraw(amt)
        print("Success")
    except NegativeAmountError:
        print("Error: Amount cannot be negative")
    except InsufficientFundsError:
        print("Error: Insufficient funds")
print(f"Final Balance: {account.balance}")