from abc import * 

class Parent(ABC):
    @abstractmethod
    def m2(self):
        pass


class Child(Parent):
    def m2(self):
        print("Child class- m2 method")

c = Child()
print(id(c))
c.m2()