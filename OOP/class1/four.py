class Account:
    def __init__(self):
        print("Const method executing!")
    def account_Details(self):
        print("Getting Account Details")


a1 = Account()
a1.account_Details()
#Account().account_Details()
