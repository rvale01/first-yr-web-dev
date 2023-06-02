import mysql.connector, dbfunc
conn = dbfunc.getConnection()   #connection to DB
DB_NAME = 'TEST_DB'             #DB Name
TABLE_NAME = 'TEST_TABLE'

SELECT_statement = 'SELECT * FROM ' + TABLE_NAME +';'   
if conn != None:    #Checking if connection is None
    if conn.is_connected(): #Checking if connection is established
        print('MySQL Connection is established')                          
        dbcursor = conn.cursor()    #Creating cursor object
        dbcursor.execute('USE {};'.format(DB_NAME)) #use database                
        dbcursor.execute(SELECT_statement)   
        print('SELECT statement executed successfully.') 
        row = dbcursor.fetchone()
        while row is not None:
            print(row, '\n')
            row = dbcursor.fetchone()                      
        dbcursor.close()              
        conn.close() #Connection must be closed
    else:
        print('DB connection error')
else:
    print('DBFunc error')
