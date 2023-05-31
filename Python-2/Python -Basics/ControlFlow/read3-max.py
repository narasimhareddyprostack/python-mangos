a  = int(input("Enter First Number:"))
b  = int(input("Enter Second Number :"))
c  = int(input("Enter Third Number:"))

if a>b and a>c:
    print("MAX value :",a)
elif b>c and b>a:
    print("MAX Value", b)
else :
    print("MAX Value:",c)
