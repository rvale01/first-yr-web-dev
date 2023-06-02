# Note: You may reuse dbfunc.py if needed. Also, Exercise2.py provides a skeleton for you to see
# how can you structure your program. You’ll need to complete functions with necessary
# functionality. Have a look at attached Exercise2.py.
# Note: If you’re using CSCT remote server for this exercise then you should use one of the
# databases created for you with your MySQL userid.
# Step 1: Create a table with table name ‘Movie’ and fields ‘movie_id {PK}’, ‘mname’ NOT NULL,
# ‘release_year’ NOT NULL.

import mysql.connector, dbfunc

conn = dbfunc.getConnection()   #connection to DB
DB_NAME = 'valentina2ronchi'             #DB Name

# step 1
def create_table(self):
    STATEMENT = "CREATE TABLE Movie (movie_id VARCHAR(10), mnane VARCHAR(10) NOT NULL, release_year VARCHAR(4) NOT NULL, PRIMARY KEY (movie_id));"

    if conn!= None:
        if conn.is_connected():
            print("Connected")
            dbcursor = conn.cursor()
            dbcursor.execute(STATEMENT)
            print("Table created")
        else:
            print("There are problems with the connection")
            exit()
    else:
        print("DBFunc error")
        exit()

# Step 2: fill Movie table with mock data. Hint: Use INSERT statement and you may choose your
# favourite movies.
def insert_static_data(self):
    STATEMENT = "INSERT INTO Movie (movie_id, mnane, release_year) VALUES (%s, %s, %s)"
    dataset = [ (1000,'Peppa Pig','2020'),
            (2000,'James Bond','2018'),
            (3000,'I do not know', '2015'),
            (4000,'Hello there','2000'),
            (5000,'random data','2016')]
    if conn != None:  # Checking if connection is None
        if conn.is_connected():  # Checking if connection is established
            dbcursor = conn.cursor()  # Creating cursor object
            dbcursor.execute('USE Movie')  # use database
            dbcursor.execute(STATEMENT, dataset)  # multiple datasets
            conn.commit()
            dbcursor.close()
            conn.close()  # Connection must be closed
        else:
            print('DB connection error')
    else:
        print('DBFunc error')

def insert_given_data(self, id, name, year):
    STATEMENT = "INSERT INTO Movie (movie_id, mnane, release_year) VALUES (%s, %s, %s)"
    dataset = (id, name, year)
    if conn != None:
        if conn.is_connected:
            dbcursor = cunn.cursor()
            dbcursor.execute('USE Movie')
            dbcursor.execute(STATEMENT,dataset)
            conn.commit()
            dbcursor.close()
            conn.close
            print("The new movie was added")
        else:
            print('DB connection error')
    else:
        print('DBFunc error')

def select_given_data(self, name, year):
    STATEMENT = "SELECT * FROM Movie WHERE name = %s AND release_year = %s"
    dataset = (name, year)
    if conn != None:
        if conn.is_connected:
            dbcursor = cunn.cursor()
            dbcursor.execute('USE Movie')
            dbcursor.execute(STATEMENT,dataset)
            row = dbcursor.fetchall()
            if row is not None:
                for value in row:
                    print(value)
            else:
                print("Movie does not exist")
            dbcursor.close()
            conn.close
        else:
            print('DB connection error')
    else:
        print('DBFunc error')

def update_given_data(self, name, year, newYear):
    STATEMENT = "UPDATE Movie SET release_year = %s WHERE name = %s AND release_year = %s"
    dataset = (newYear, name, year)
    if conn != None:
        if conn.is_connected:
            dbcursor = cunn.cursor()
            dbcursor.execute('USE Movie')
            dbcursor.execute(STATEMENT,dataset)
            conn.commit()   
            print("Changed done")
            dbcursor.close()
            conn.close
        else:
            print('DB connection error')
    else:
        print('DBFunc error')

def delete_given_data(self, name, year):
    STATEMENT = "DELETE FROM Movie WHERE name = %s AND release_year = %s"
    dataset = (name, year)
    if conn != None:
        if conn.is_connected:
            dbcursor = cunn.cursor()
            dbcursor.execute('USE Movie')
            dbcursor.execute(STATEMENT,dataset)
            conn.commit()   
            print("Changed done")
            dbcursor.close()
            conn.close
        else:
            print('DB connection error')
    else:
        print('DBFunc error')




# Step 3: Your program offers end user four options: 1. Add movie, 2. Retrieve movie, 3. Update
# movie, 4. Remove movie, 5. Quit

def menu(self):
    print("Menu:\n1. Add movie\n2. Retrieve movie\n3. Update movie\n4. Remove movie\n5. Quit")
    choice = input(int(""))
    # 3.1 - When user enters 1, your program should ask for movie name and release year and
    # should add it in the Movie table.
    if(choice == 1):
        name = input(str("Name: "))
        year = input(str("Release year: "))
        id = input(int("ID: "))
        insert_given_data(id, name, year)
    elif(choice == 2):
        name = input(str("Name: "))
        year = input(str("Release year: "))
        select_given_data(id, name, year)
    elif(choice == 3):
        name = input(str("Name: "))
        year = input(str("Release year: "))
        update_given_data(id, name, year)
    elif(choice == 4):
        name = input(str("Name: "))
        year = input(str("Release year: "))
        delete_given_data(id, name, year)
    elif(choice == 5):
        print ('Good bye! Hope to see you soon...')
        conn.close()
        exit()
    else:
        print("Invalid input!")

# 3.1.1 – Program should show a success message after adding movie to DB.
# 3.1.2 - Optional step: Add error handling e.g., if movie name and release date is
# already in Movie table then a suitable message should be displayed and
# duplicate record should not be added.
# 3.2 - When user enters 2, your program should ask for movie name and perform select
# statement to retrieve movie details and display on screen. Display an appropriate error
# message if movie does not exist.
# 3.3 – When user enters 3, your program should for ask for movie name and updated
# release date and update the release date for the selected movie it in the database.
# 3.4 – When user enters 4, your program should for ask for movie name and release date
# and delete the matching record from the database.
# 3.5 – Quit from the program
menu()