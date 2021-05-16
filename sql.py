from itertools import product
import xlrd
import mysql.connector as mariadb
import DBManager
import csv
import pandas as pd

mariadb_connection=mariadb.connect(user="root",password="",host="Localhost",port="3306")

create_cursor = mariadb_connection.cursor()
def synolikes_afikseis_touristwn (year,row,col,total_arrivals,sheet):

    #h sthlh me tis synolikes afikseis ths swsths xronias einai 2 sthles dipla apo thn sthlh pou periexei to geniko synolo
    tourists = round(sheet.cell_value(row, col + 2))
    sql = "INSERT IGNORE INTO tourism_per_year (year,total_tourists) VALUES(%s,%s)"
    val = (year,tourists)
    cursor.execute(sql,val)
    db.mydb.commit()
    print("Sucessful Parse of Data in table tourism_per_year")
    csv_output_file(['ΕΤΟΣ','ΣΥΝΟΛΙΚΟΙ ΤΟΥΡΙΣΤΕΣ'],"ΣΥΝΟΛΙΚΕΣ ΑΦΙΞΕΙΣ ΤΟΥΡΙΣΤΩΝ ΓΙΑ ΤΟ 2011-2013.csv","tourism_per_year")

 


