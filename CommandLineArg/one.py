from sys import argv


print(argv[1:])
list = argv[1:]

sum = 0
for ele in list:
    sum = sum+int(ele)

print(sum)
