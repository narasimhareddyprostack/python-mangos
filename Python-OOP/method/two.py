class Test:
    @classmethod
    def m2(cls):
        cls.c =200
        Test.d=400

t1=Test()
t2=Test()
Test.m2()
print(Test.__dict__)
print(t1.__dict__)
print(t2.__dict__)

#How access static variable

print(t1.c)   #300
print(t1.d)   #400
print(Test.d) #400