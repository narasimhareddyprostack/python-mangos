#binary file mode 

f = open("loc.jpeg","rb")
data = f.read()

f1 = open("psa.jpeg","wb")
f1.write(data)

print("Created Successfully")