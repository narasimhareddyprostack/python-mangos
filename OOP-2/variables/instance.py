class Test:
    def __init__(self):
        self.a=10
        self.b=20
    def m1(self):
        self.c=30


  

t1=Test()
print(t1.__dict__)
t1.f=60
t1.m1()
print(t1.__dict__)


t2 = Test()
print(t2.__dict__)
t2.f = 600
t2.m1()
print(t2.__dict__)
