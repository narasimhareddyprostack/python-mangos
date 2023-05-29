class Test:
    def __init__(self):
        self.a= 100
    def m1(self):
        self.b= 200
t1 =Test()
t1.m1()

t1.c= 300
t1.a = 150

t2 =Test()
t2.d= 400
print(t1.__dict__)
print(t2.__dict__)

