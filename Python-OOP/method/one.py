class Test:
    
    def m1(self):
        self.a = 100
        self.b = 200


t1 = Test()
t2 = Test()
t1.m1()
t2.m1()

print(t1.__dict__)
print(t2.__dict__)
