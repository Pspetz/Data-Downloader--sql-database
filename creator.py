import mysql.connector as mariadb

mariadb_connection=mariadb.connect(user="root",password="",host="Localhost",port="3306",database="Tourism_Statistics")
create_cursor = mariadb_connection.cursor()
create_cursor.execute("CREATE TABLE  IF NOT EXISTS tourism_per_year(year INT NOT NULL PRIMARY KEY,total_tourists INT)")

for x in create_cursor:
    print(x)
