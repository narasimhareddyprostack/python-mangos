try:
    f = open('abc.txt', 'r')
except:
    print("exception raised")
    f = open("one.txt",'r')


print(f.read())