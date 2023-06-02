import mysql.connector
from mysql.connector import errorcode
 
# MYSQL CONFIG VARIABLES
hostname    = "localhost"
username    = "valentina2ronchi"
passwd  = "Valentina2ronchI+$++"



def getConnection():    
    try:
        conn = mysql.connector.connect(host='localhost',                              
                              user='valentina2ronchi',
                              password='Valentina2ronchI16+$++',
                              port='3307')  
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('User name or Password is not working')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print('Database does not exist')
        else:
            print(err)                        
    else:  #will execute if there is no exception raised in try block
        return conn   
                
