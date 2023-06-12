try:
    a = int(input("Enter First Number:"))
    b = int(input("Enter Second Number:"))
    print(a/b)
except:
    print("Alternate sys")
except ZeroDivisionError as msg:
    print(msg)
except ValueError as msg:
    print(msg)


print("Good Night")
