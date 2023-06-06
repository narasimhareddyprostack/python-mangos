#abstraction - never talks about implementation
#abstract class
#abstract method
#interface
#from abc import ABC, abstractmethod
from abc import *
class Account(ABC):
    
    @abstractmethod
    def get_Min_Bal(self):
        pass

    def get_Details(self):
        print("Account Details")

class SA(Account):
    def get_Min_Bal(self):
        return 500
a = SA()
a.get_Details()
print(a.get_Min_Bal())