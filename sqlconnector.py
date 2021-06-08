import mysql.connector as mariadb


mariadb_connection=mariadb.connect(user="root",password="",host="Localhost",port="3306")

create_cursor = mariadb_connection.cursor()


create_cursor.execute("CREATE DATABASE IF NOT EXISTS Greece_stats;")
for x in create_cursor:
    print(x)

