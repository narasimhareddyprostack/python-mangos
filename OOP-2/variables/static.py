class Test:
    a = 100
    def __init__(self):
        self.z=999
        Test.b=200
    def m1(self):
        Test.c=300
    @classmethod
    def m2(cls):
        Test.d=400
        cls.e= 500
    @staticmethod
    def m3():
        Test.f = 600


t1=Test()
print(t1.__dict__) # {}
t1.m1()
t1.m2()
t1.m3()
print(Test.__dict__)