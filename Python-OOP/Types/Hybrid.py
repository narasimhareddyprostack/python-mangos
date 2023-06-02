class GP1:
    def m1(self):
        print("GP1 class-m1() method")
class GP2:
    def m2(self):
        print("GP2 class-m2() method")
class Parent(GP1,GP2):
    def m3(self):
        print("Parent class-m3() method")
class Child1(Parent):
    def m4(self):
        print("Child1 class-m4() method")
class Child2(Parent):
    def m5(self):
        print("Child2 class-m5() method")

obj1 = Child1()
obj1.m1()
obj1.m2()
obj1.m3()
obj1.m4()
obj2 = Child2()
obj2.m1()
obj2.m2()
obj2.m3()
obj2.m5()