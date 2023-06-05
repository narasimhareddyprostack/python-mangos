from abc import * 

class Parent(ABC):
    @abstractmethod
    def m2(self):
        pass

p=Parent()  
print(id(p))