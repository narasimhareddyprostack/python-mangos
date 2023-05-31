class Emp:
    '''' This document String '''

    def __init__(self):
        print(id(self))

e = Emp()
print(id(e))   # 17226896
