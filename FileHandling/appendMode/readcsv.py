import csv 
f = open('data.csv','r')
data=csv.reader(f)

for line in data:
    print(line)