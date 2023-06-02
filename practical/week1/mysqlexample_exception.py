import mysql.connector
from mysql.connector import Error
 
""" Connect to MySQL database """
try:
    conn = mysql.connector.connect(host='127.0.0.1',                              
                              user='zaheer',
                              password='SecretPassword')  
except Error as e:
    print(e)
else:  #will execute if there is no exception raised in try block
    if conn.is_connected():
        print('MySQL Connection is established')
        # Write your DB queries here...         
    conn.close() #Connection must be closed



