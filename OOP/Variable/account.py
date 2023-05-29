class Account:
    min_Bal = 500

    def __init__(self,eId,eName):
        self.eId= eId
        self.eName = eName

    def deposit_Amount(self):
        self.Amount = 1000

a1=Account(101, "Rahul")
a2=Account(102, "Priyana")
a1.deposit_Amount()
a2.deposit_Amount()
a2.Amount = 666
print(a1.__dict__)
print(a2.__dict__)
print(Account.__dict__)