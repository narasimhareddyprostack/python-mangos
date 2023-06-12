
try:
    f = open('two.txt','r')
    data=f.read()
    print(data)
except:
    print("File Not Available! Please check")

finally:
    print("finally block will execute awlays ")
    #f.close()