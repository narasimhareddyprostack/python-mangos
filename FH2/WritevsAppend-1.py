f = open("data.txt", 'r')
data = f.read()

f1 = open("account.txt", 'w')
f1.write(data)

print("Written Successfully")