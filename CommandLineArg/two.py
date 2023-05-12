# read CLA and print sum of CLA elemetns
from sys import argv
newList = []
list = argv[1:]
print(list)

for l in list:
    newList.append(int(l))

print(newList)
""" list = argv[1:]
print(newList) """


print(sum(newList))
