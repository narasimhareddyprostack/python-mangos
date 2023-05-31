""" 
print(round(9.4))
print(round(9.8)) """


bata_Prices=[7.88, 9.44343, 5.6554, 99.45455]

#expected [8, 9, 6,99]


map_Obj=map(round, bata_Prices)
rounded_Prices = list(map_Obj)
print(rounded_Prices)
