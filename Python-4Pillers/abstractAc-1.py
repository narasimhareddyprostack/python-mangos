#abstraction - never talks about implementation
#abstract class
#abstract method
#interface
from abc import ABC
class Account(ABC):
    pass


a = Account()
print(id(a))
print(a)