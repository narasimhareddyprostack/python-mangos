from abc import *
class Test:
    @abstractmethod
    def m1():
        pass

t = Test()
print(id(t))