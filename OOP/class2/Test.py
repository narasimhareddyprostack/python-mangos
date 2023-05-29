class Test:
    def __init__(self):
        print(id(self))

    def getInstance(self):
        print(id(self))


t1 = Test()
t1.getInstance()
print(id(t1))

#what is t1 ?  - t1 is ref variable to refer class memmber outside a class
#what is self  -   self - is pointer variable to refer class member inside a class
