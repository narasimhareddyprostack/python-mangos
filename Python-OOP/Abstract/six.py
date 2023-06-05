from abc import * 

class Account(ABC):
    @abstractmethod
    def get_Min_Bal(self):
        pass

