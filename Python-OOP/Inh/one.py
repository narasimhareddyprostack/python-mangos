class Parent:
    def m1(self):
        print("Parent class - m1()")
    def m2(self):
        print("Parent class - m2()")

class Child(Parent):
    def m3(self):
        print("Child class - m3()")

c=Child()
c.m1()
c.m2()
c.m3()
