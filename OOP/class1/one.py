class Emp:
    pass


e1= Emp()
e1.id = 101

e2 = Emp()

print(e1)
print(id(e1))
print(e1.__dict__)