import mysql.connector
try:
    conn = mysql.connector.connect(host='localhost', database='prostack', user='root', password='root')
    print(conn.is_connected())
    
    sql_select_Query = "select * from empone"

    cursor = conn.cursor()
    
    cursor.execute(sql_select_Query)
    # get all records
    
    records = cursor.fetchall()
    print("Total number of rows in table: ", cursor.rowcount)

    print("\nPrinting each row")
    for row in records:
        print("Id = ", row[0], )
        print("Name = ", row[1])
        print("Sal  = ", row[2])
    
   
    
except Error as e:
    print(e)
