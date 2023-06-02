import mysql.connector, dbfunc
conn = dbfunc.getConnection()   #connection to DB
DB_NAME = 'TEST_DB'             #DB Name
TABLE_NAME = 'TEST_TABLE'

def iter_row(cursor, size=10):
    while True:
        rows = cursor.fetchmany(size)
        if not rows:
            break
        for row in rows:
            yield row

SELECT_statement = 'SELECT * FROM ' + TABLE_NAME +';'   
if conn != None:    #Checking if connection is None
    if conn.is_connected(): #Checking if connection is established
        print('MySQL Connection is established')                          
        dbcursor = conn.cursor()    #Creating cursor object
        dbcursor.execute('USE {};'.format(DB_NAME)) #use database                
        dbcursor.execute(SELECT_statement)   
        print('SELECT statement executed successfully.') 
        for row in iter_row(dbcursor, 5):
            print(row)                                
        dbcursor.close()              
        conn.close() #Connection must be closed
    else:
        print('DB connection error')
else:
    print('DBFunc error')
