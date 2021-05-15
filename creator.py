import mysql.connector as mariadb

mariadb_connection=mariadb.connect(user="root",password="",host="Localhost",port="3306",database="Tourism_Statistics")
create_cursor = mariadb_connection.cursor()
create_cursor.execute("CREATE TABLE  IF NOT EXISTS tourism_per_year(year INT NOT NULL PRIMARY KEY,total_tourists INT)")
create_cursor.execute("CREATE TABLE  IF NOT EXISTS country_most_tourists(year INT NOT NULL PRIMARY KEY,country VARCHAR(50),percentage FLOAT)")
create_cursor.execute("CREATE TABLE  IF NOT EXISTS tourists_by_means(year INT NOT NULL PRIMARY KEY,by_air INT,by_train INT,by_sea INT,by_road INT)")
create_cursor.execute("CREATE TABLE  IF NOT EXISTS tourism_per_semester(year INT NOT NULL,semester INT NOT NULL ,total_tourists INT, CONSTRAINT TOUR_SEM PRIMARY KEY (year,semester))")

for x in create_cursor:
    print(x)

