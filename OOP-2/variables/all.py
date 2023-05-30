class Test:
    a = 10   #static variable 
    def __init__(self):
        self.b=20
        self.c=30


t1= Test()

print(t1.__dict__)
print(Test.__dict__)