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


a = Account()
print(id(a))
print(a)
