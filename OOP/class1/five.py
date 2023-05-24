class Account:
    def __init__(self,id,name, amount):
        self.accId = id
        self.accName=name
        self.accAmouont=amount
    def acc_Details(self):
        print("Account Name:", self.accName)



a1 = Account(101, "Rahul", 50000)
print(a1.__dict__)
a1.acc_Details()
a1.acc_Details()
a1.acc_Details()
a1.acc_Details()
a1.acc_Details()