import csv
f  = open("dev.csv", "w" , newline="")
cp =csv.writer(f)
cp.writerow(["Id","Name","Salary"])

noOfEmp  = int(input("Enter No of Employees:::: "))

for i in range(noOfEmp):
    eId=input("Enter Id:")
    eName=input("Enter Name:")
    eSal = input("Salary")
    cp.writerow([eId,eName,eSal]    )


#business logic

f.close()
