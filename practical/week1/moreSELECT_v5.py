import mysql.connector, dbfunc
conn = dbfunc.getConnection()   #connection to DB
DB_NAME = 'STUDENTSREG'             #DB Name
#List all students who were enrolled on "Web Programming" 
# in academic year 2014-2015
SELECT_statement = "SELECT s.SID, s.SName, e.ACAD_YEAR, m.MID, m.MName \
FROM STUDENT s, MODULES m, STUDENT_ENROLEMENT e \
WHERE s.SID = e.SID AND e.MID = m.MID AND m.MNAME \
    = 'Web Programming' AND e.ACAD_YEAR =  '2014-2015' \
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
