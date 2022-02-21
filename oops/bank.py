class Amount:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self,dep_amount):
        self.balance = self.balance +  dep_amount
        print(f"Added {dep_amount} To your bank account")
    def withdrawl(self,wt_amt):
        if self.deposit >= wt_amt:
            print(f"WithDrawed Amount {wt_amt} and remaining balance {self.balance - wt_amt} ")
            self.balance = self.balance - wt_amt
        else:
            print("You Have Insufficient Funds")
    def __str__(self):
        return f"Owner : {self.owner} \n Balance  :- {self.balance}"