import csv

f = open("data.csv", 'r')

data = csv.reader(f)

#print(list(data))
for line in list(data):
    for word in line:
        print(word,"\t", end="")
    print()