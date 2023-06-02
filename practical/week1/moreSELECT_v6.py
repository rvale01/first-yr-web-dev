import mysql.connector, dbfunc
conn = dbfunc.getConnection()   #connection to DB
DB_NAME = 'STUDENTSREG'             #DB Name
#list how any modules each student took in every academic year
SELECT_statement = "SELECT s.SID, s.SName, e.ACAD_YEAR, \
    COUNT(e.MID) as totalmodules \
    FROM STUDENT s JOIN STUDENT_ENROLEMENT e ON s.SID = e.SID \
    GROUP By s.SID, s.SName, e.ACAD_YEAR  \
    ORDER By s.SID;"

if conn != None:    #Checking if connection is None
    if conn.is_connected(): #Checking if connection is established
        print('MySQL Connection is established')                          
        dbcursor = conn.cursor()    #Creating cursor object
        dbcursor.execute('USE {};'.format(DB_NAME)) #use database                
        dbcursor.execute(SELECT_statement)   
        print('SELECT statement executed successfully.') 
        rows = dbcursor.fetchall()
        print('Total rows: ', dbcursor.rowcount)
        for row in rows:
            print(row)                                
        dbcursor.close()              
        conn.close() #Connection must be closed
    else:
        print('DB connection error')
else:
    print('DBFunc error')
