import mysql.connector, dbfunc
conn = dbfunc.getConnection()   #connection to DB
DB_NAME = 'TEST_DB'             #DB Name
TABLE_NAME = 'TEST_TABLE'
tid = input('Enter TempID: ')
name = input('Enter Name: ')
address = input('Enter Address: ')
# here you should perform data validation syntax/semantics 
UPDATE_statement = 'UPDATE ' + TABLE_NAME + ' SET \
    Name = %s, \
    ADDRESS = %s \
    WHERE tempId = ' + tid + ';'    

if conn != None:    #Checking if connection is None
    if conn.is_connected(): #Checking if connection is established
        print('MySQL Connection is established')                          
        dbcursor = conn.cursor()    #Creating cursor object
        dbcursor.execute('USE {};'.format(DB_NAME)) #use database        
        dataset = (name, address)        
        dbcursor.execute(UPDATE_statement, dataset)   
        conn.commit()              
        print('UPDATE statement executed successfully.') 
        dbcursor.close()              
        conn.close() #Connection must be closed
    else:
        print('DB connection error')
else:
    print('DBFunc error')
