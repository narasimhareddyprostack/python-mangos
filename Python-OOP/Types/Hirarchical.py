class Parent:
    def m1(self):
        print("Parent class -m1() method")
    def m2(self):
        print("Parent class -m2() method")
class Child1(Parent):
    def m3(self):
        print("Child1 class -m3() method")
class Child2(Parent):
    def m4(self):
        print("Child2 class -m4() method")

obj1=Child1()
obj1.m1()
obj1.m2()
obj1.m3()
#obj1.m4()   - Child1 - object has no attribute m4
obj2=Child2()
obj2.m1()
obj2.m2()
#obj2.m3()  - Child2 object has no attribute m3
obj2.m4()
