from abc import *

class Test(ABC):

    def m1(self):
        print("Test Class m1 () method - instance")
    @classmethod
    def m2(cls):
        pass 
    @abstractmethod
    def m3(self):
        pass 
t = Test()