from itertools import product
import xlrd
import mysql.connector as mariadb
import DBManager
import csv
import pandas as pd

mariadb_connection=mariadb.connect(user="root",password="",host="Localhost",port="3306",database="Greece_Stats")

create_cursor = mariadb_connection.cursor()
def synolikes_afikseis_touristwn (year,row,col,total_arrivals,sheet):

 
    tourists = round(sheet.cell_value(row, col + 2))
    sql = "INSERT INTO statistika (year,total_tourists) VALUES(%s,%s)"
    val = (year,tourists)
    cursor.execute(sql,val)
    db.mydb.commit()
    print("Epituximeno perasma statistikos sthn vasi Greece_Stats")
    csv_output_file(['XRONOLOGIA','TOURISTES'],"ΣΥΝΟΛΙΚΕΣ ΑΦΙΞΕΙΣ ΤΟΥΡΙΣΤΩΝ ΓΙΑ ΤΟ 2015-2019.csv","statistika")

 


