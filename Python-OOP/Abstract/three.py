from abc import *

class Parent(ABC):
    pass

p = Parent()

print(id(p))