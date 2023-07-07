import mysql.connector 
try:
    con = mysql.connector.connect(host='localhost', database='prostack', user='root',password='root')
    print(con.is_connected())

    #create db cursor object
    dbcor=con.cursor()
    dbcor.execute('insert into empOne values(102,"Sonia",550000)')
    dbcor.execute('insert into empOne values(103,"Priyanka",550000)')

    con.commit()
    print("Data Inserted successfully")
except Error as e:
    print("except")
    print("Error while connecting to MySQL", e)
