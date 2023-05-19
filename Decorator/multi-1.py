def verifySecondValue(func):
    def inner(a,b):
        if b == 0:
            print("Cant Divide by Zero")
        else:
            return func(a,b)
    return inner




@verifySecondValue
def calc(a,b):
    return a/b



print(calc(10,5))
print(calc(10,0))