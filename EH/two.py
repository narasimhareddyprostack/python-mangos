print('GM')
a = int(input("Enter First No:"))
b = int(input("Enter Second No:"))
try:
    print(a/b)
except:
    print("Exception Raised - alternate executing")
    print(a/5)
print("GN")
