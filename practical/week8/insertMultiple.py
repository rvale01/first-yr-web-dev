import mysql.connector, dbfunc
conn = dbfunc.getConnection()   #connection to DB
DB_NAME = 'TEST_DB'             #DB Name
TABLE_NAME = 'TUTOR'
INSERT_statement = 'INSERT INTO ' + TABLE_NAME + ' (\
    Tut_Id, TName, DoB, HOURS) VALUES (%s, %s, %s, %s);'    
if conn != None:    #Checking if connection is None
    if conn.is_connected(): #Checking if connection is established
        print('MySQL Connection is established')                          
        dbcursor = conn.cursor()    #Creating cursor object
        dbcursor.execute('USE {};'.format(DB_NAME)) #use database        
        dataset = [ (1000,'David Wyatt','1982/01/01',4),
            (1001,'Raj Ramachandran','1987/02/03',3),
            (1002,'Kamran Soomro','1985/04/13',4),
            (1003,'David Ludlow','1950/01/16',1),
            (1004,'Zaheer Khan','1979/08/31',None),
            (1005,'Djamel Djnouri','1981/06/30',None),
            (1006,'Elias Piminides','1969/03/27',None),
            (1007,'Kamran Soomro','1965/11/05',None),
            (1008,'Barkha Javed','1995/11/11',None),
            (1009,'James Lear','1993/02/12',None) ]        
        dbcursor.executemany(INSERT_statement, dataset) #multiple datasets  
        conn.commit()              
        print('INSERT query executed successfully.') 
        dbcursor.close()              
        conn.close() #Connection must be closed
    else:
        print('DB connection error')
else:
    print('DBFunc error')
