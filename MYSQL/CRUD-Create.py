import mysql.connector

#create connection obj
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='prostack',
                                         user='root',
                                         password='root')
    print(connection.is_connected())
    dbcursor = connection.cursor()
    sql_St = "create table empone(id int, name varchar(32), sal int)"
    dbcursor.execute(sql_St)
    print('Table created ')
except Error as e:
    print("except")
    print("Error while connecting to MySQL", e)
