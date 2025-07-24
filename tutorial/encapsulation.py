class BankBalance:
    def __init__(self):
        self._balance = 0.0

    @property
    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Cannot insert negative amount")
        self._balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Cannot withdraw negative amount")
        if amount > self._balance:
            raise ValueError("Insufficient balance")
        self._balance -= amount

account1 = BankBalance()
print(account1.balance)
account1.deposit(200)
print(account1.balance)
account1.withdraw(55)

print(account1.balance)











