a  = int(input("Enter First Number:"))
b  = int(input("Enter Second Number :"))
c  = int(input("Enter Third Number"))

if a<b and a<c:
    print("Min value :",a)
elif b<c and b<a:
    print("Min Value", b)
else :
    print("Min Value:",c)