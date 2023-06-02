import mysql.connector, dbfunc

conn = dbfunc.getConnection()   #connection to DB
DB_NAME = 'TEST_DB'             #DB Name
TABLE_NAME = 'Movie'

def create_Table():
    TABLE_DESCRIPTION = 'CREATE TABLE ' + TABLE_NAME + ' ( \
        movie_id VARCHAR(10), \
        mname VARCHAR(40) NOT NULL, \
        release_year VARCHAR(4), \
        PRIMARY KEY (movie_id));'
    if conn != None:    #Checking if connection is None
        if conn.is_connected(): #Checking if connection is established
            print('MySQL Connection is established')                          
            dbcursor = conn.cursor()    #Creating cursor object
            dbcursor.execute('USE {};'.format(DB_NAME)) #use database    
            dbcursor.execute('DROP TABLE IF EXISTS {};'.format(TABLE_NAME)) #Think why is this statement here? Is this good program design?   
            dbcursor.execute(TABLE_DESCRIPTION) 
            print('Table {} created successfully.'.format(TABLE_NAME))            
               
            #conn.close() #Connection must be closed but if you need to perform other db operations 
            #then keep it open and close when quitting the program
        else:
            print('DB connection error')
            exit()
    else:
        print('DBFunc error')
        exit()


def fillMockData():
    print('This function adds mock data to movie table')
    #The code for inserting mockdata should go here... change the definition of this function as appropriate. 
    #You can use insert statement and add multiple records...

def addMovie():
    print('This function adds movie and displays success or error message on the screen')
    #The code for add movie should go here... change the definition of this function as appropriate. 

def retrieveMovie():
    print('This function retrieves a movie record and displays it on the screen')
    #The code for retrieve movie should go here... change the definition of this function as appropriate. 

def updateMovie():
    print('This function updates a movie record and displays appropriate message on the screen')
    #The code for update movie should go here... change the definition of this function as appropriate. 

def deleteMovie():
    print('This function deletes a movie record and displays appropriate message on the screen')
    #The code for delete movie should go here... change the definition of this function as appropriate. 


print('Welcome to Movie management system')
#Creating Movie table -- you need to think what will happen when we run this program again... 
# and importance of drop table... but is it efficient program design?
create_Table()

#filling Movie table with mock data
fillMockData()

print ('Select one of the following options: \n1. Add movie \n2. Retrieve movie \n3. Update movie, \n4. Remove movie \n5. Quit \n')
choice = int(input('Enter choice (1-5): '))

if choice == 1:
    addMovie()
    conn.close()
elif choice == 2:
    retrieveMovie()
    conn.close()
elif choice == 3:
    updateMovie()
    conn.close()
elif choice == 4:    
    deleteMovie()
    conn.close()
else:
    print ('Good bye! Hope to see you soon...')
    conn.close()
    exit()



