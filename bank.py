class Account:
    #constructor
    def __init__(self, bal, acc_no):
        self.bal = bal;
        self.acc_no = acc_no
    
    #debit method
    def debit(self, amount):
        self.bal -= amount
        print(f"{amount} was debited from {self.acc_no}") 
        print(f"total balance: {self.get_balance()}")
    
    #credit method
    def credit(self, amount):
        self.bal += amount
        print(f"{amount} was credited to {self.acc_no}")
        print(f"total balance: {self.get_balance()}")
    
    #get balance
    def get_balance(self):
        return self.bal

acc1 = Account(200, 456775)
acc1.debit(200)
acc1.credit(100)
acc1.get_balance()
print(acc1.bal, acc1.acc_no)
