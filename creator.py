import mysql.connector as mariadb

mariadb_connection=mariadb.connect(user="root",password="",host="Localhost",port="3306",database="Greece_stats")
create_cursor = mariadb_connection.cursor()
create_cursor.execute("CREATE TABLE  IF NOT EXISTS statistika(year INT NOT NULL PRIMARY KEY,tourists INT)")

for x in create_cursor:
    print(x)
