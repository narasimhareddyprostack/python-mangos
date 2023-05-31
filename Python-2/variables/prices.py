
a = 10    # a is global scope 

def m1():
    global b
    b = 20  # local variable
    print(a) #10
    print(b) #20

def m2():
    print(a)  #10
    print(b)  #20

def m3():
    print(a)  # 10

m1()
m2()
m3()
