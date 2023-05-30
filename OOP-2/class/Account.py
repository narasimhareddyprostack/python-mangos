class Account:
    min_Bal = 500
    def __init__(self,id,name,amount):
        self.acc_Id = id 
        self.acc_Name= name 
        self.acc_Amount = amount 

    def open_Account(self):
        print("Account Opended Successfully")
    def deposit_Amount(self,amount):
        print(amount , ":Amount Deposited")


a1=Account(101, "Rahul", 15000)
a2=Account(102, "Sonai", 25000)
a3=Account(103, "Priyanka", 35000)
#a1.open_Account()
#a1.deposit_Amount(5000)

print(a1.__dict__)
print(a2.__dict__)
print(a3.__dict__)
