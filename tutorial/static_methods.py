#static methods belongs to class itself rather than any instance of the class

class BankAccount:
    min_balance = 100

    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance
    
    def deposit(self, amount):
        if self._is_valid_amount(amount):
            self._balance += amount
            #this way you call a private or protected method
            self.__log_transaction(amount, "deposit")
            print(f"{self.owner}'s new balance : ${self._balance}")
        else:
            print("Deposit amount must be positive")
    
    #protected method
    def _is_valid_amount(self, amount):
        return amount>0

    #private method
    def __log_transaction(self, amount, transaction_type):
        print(f"Logging {transaction_type} of ${amount}. New balance : {self._balance}")

    @staticmethod
    def is_valid_interest_rate(rate):
        return 0 <= rate <= 5


account1 = BankAccount('Yash', 500)
account1.deposit(200)
#this method is accessible using both the class name and the instance name
print(BankAccount.is_valid_interest_rate(7))
print(account1.is_valid_interest_rate(4))








