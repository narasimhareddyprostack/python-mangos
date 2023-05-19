
def smart_Div(func):
    def inner(a,b):
        if b == 0:
            print("Cant Divibe by Zero")
        else:
            return func(a,b)
    return inner


def calc(a,b):
    return a/b


d = smart_Div(calc)

print(d(10,5))
print(d(10,0))