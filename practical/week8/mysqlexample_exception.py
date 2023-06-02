import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
 
""" Connect to MySQL database """
try:
    conn = mysql.connector.connect(host='localhost',                              
                              user='valentina2ronchi',
                              password='Valentina2ronchI16+$++',
                              port='3307')  
except Error as e:
    print(e)
else:  #will execute if there is no exception raised in try block
    if conn.is_connected():
        print('MySQL Connection is established')
        # Write your DB queries here...         
    conn.close() #Connection must be closed



