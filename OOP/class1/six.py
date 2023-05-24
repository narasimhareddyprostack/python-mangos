class Account:
    def __init__(self,id,name,amount):
        self.id = id 
        self.name =name
        self.amount = amount

    def get_Account_Info(self):
        self.email = 'Rahul@pm.com'


a1 = Account(101, "Rahul", 60000)
a1.get_Account_Info()
a1.loc = "Wayanad"

print(a1.__dict__)