class Test:
    __a = 100  #private variable
    _b=200     #protected
    c=300      #public

    def __init__(self):
        print(self.__a)
        print(self._b)
        print(self.c)

    def get_Data(self):
        return self.__a

t = Test()
print(t.c)
print(t._b)
print(t.get_Data())
