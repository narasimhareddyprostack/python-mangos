class Test:
    a = 100

    def __init__(self):
        self.b=200
    def m1(self):
        self.c= 300
    @classmethod
    def m2(cls):
        cls.d=400
    @staticmethod
    def m3():
        Test.e = 500

t1=Test()
t1.m1()
t1.m2()
t1.m3()

print(t1.__dict__)
print(Test.__dict__)