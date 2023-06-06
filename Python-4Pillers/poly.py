class Test:

    def m1(self, a, b):
        print("m1 with two arg")

    def m1(self):
        print("m1 method")

    def m1(self,a):
        print("m1() with arg")



t = Test()

t.m1(10)
