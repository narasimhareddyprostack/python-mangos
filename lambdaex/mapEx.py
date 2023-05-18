dob_Year=[1983,1993,2003]

def cal_Age(year):
    return 2023-year

map_obj=map(cal_Age, dob_Year)

print(map_obj)
print(list(map_obj))


