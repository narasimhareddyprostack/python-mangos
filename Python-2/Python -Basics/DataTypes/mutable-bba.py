l = [38,40,42,44]

b = bytes(l)
ba= bytearray(l)

#b[0] = 39
ba[0] = 39
#bytes - immutable
#bytearray - mutable
for x in ba:
    print(x)