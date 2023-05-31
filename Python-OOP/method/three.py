class Test:
    count = 0   #static
    def __init__(self):
        Test.count = Test.count +1

    @classmethod
    def noOfObject(cls):
        print(cls.count)
t1=Test()
t2=Test()
t3=Test()
t4=Test()
t5=Test()

Test.noOfObject()