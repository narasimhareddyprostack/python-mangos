#from abc import * 

class Account(ABC):

    @abstractmethod
    def get_Min_Bal(self):
        pass

#a=Account()
#print(a.get_Min_Bal())

class SA(Account):
    
    def get_Min_Bal(self):
        return 500

    def open_Account(self):
        print("Account opened successfully")

a1=SA()
print(a1.get_Min_Bal())
a1.open_Account()

class CA(Account):
    def get_Min_Bal(self):
        return 25000

a2=CA()
print(a2.get_Min_Bal())