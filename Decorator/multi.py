
def smart_Div(func):
    def inner(a,b):
        if b == 0:
            print("Cant Divibe by Zero")
        else:
            return func(a,b)
    return inner

@smart_Div
def calc(a,b):
    return a/b



print(calc(10,5))
print(calc(10,0))