import mysql.connector
from flask import Flask, render_template, request

app = Flask(__name__)

def get_connection():
    conn = mysql.connector.connect(host='localhost',                              
                              user='valentina2ronchi',
                              password='Valentina2ronchI16+$++',
                              port='3307',
                              database='STUDENTSREG')
    return conn
 
@app.route('/')
def index():
   return render_template('basicdbformexample.html')

@app.route('/show_list/')
def show_list():
    #fetch all tutors
    conn = get_connection()
    if conn != None:    #Checking if connection is None
        if conn.is_connected(): #Checking if connection is established
            print('MySQL Connection is established')                          
            dbcursor = conn.cursor()    #Creating cursor object            
            dbcursor.execute('SELECT * FROM TUTOR;')   
            print('SELECT statement executed successfully.')             
            rows = dbcursor.fetchall()                                    
            dbcursor.close()              
            conn.close() #Connection must be closed
            return render_template('showalltutors.html', resultset=rows)
        else:
            print('DB connection Error')
            return 'DB Connection Error'
    else:
        print('DB Connection Error')
        return 'DB Connection Error'
    
@app.route('/show_tutor', methods=['POST', 'GET'])
def show_turor():
    #fetch from database with where clause  
    if request.method == 'GET':
        tutorid = request.args.get('tutorid')
        if tutorid != None:
            conn = get_connection()
            if conn != None:    #Checking if connection is None
                if conn.is_connected(): #Checking if connection is established
                    print('MySQL Connection is established')                          
                    dbcursor = conn.cursor()    #Creating cursor object            
                    SQL_statement = 'SELECT * from TUTOR WHERE Tut_id = %s;'
                    args = (tutorid,)
                    dbcursor.execute(SQL_statement,args)
                    print('SELECT statement executed successfully.')             
                    rows = dbcursor.fetchall()                                    
                    dbcursor.close()              
                    conn.close() #Connection must be closed
                    return render_template('showtutordetails.html', resultset=rows)
                else:
                    print('DB connection Error')
                    return 'DB Connection Error'
            else:
                print('DB Connection Error')
                return 'DB Connection Error'
        else:
            print('Invalid tutor id received')
            return render_template('basicdbformexample.html')  

@app.route('/add_tutor/', methods=['POST', 'GET'])
def add_tutor():     
    if request.method == 'GET':
        tutorid = request.args.get('tutorid')
        tutorname = request.args.get('tutorname')
        tutordob = request.args.get('tutordob')
        tutorhours = request.args.get('tutorhours')
        if tutorid != None and tutorname != None and tutordob != None :
            conn = get_connection()
            if conn != None:    #Checking if connection is None
                if conn.is_connected(): #Checking if connection is established
                    print('MySQL Connection is established')                          
                    dbcursor = conn.cursor()    #Creating cursor object            
                    SQL_statement = 'INSERT INTO TUTOR VALUES (%s, %s, %s, %s);'
                    if tutorhours == 'None':
                        tutorhours = None;
                    args = (tutorid,tutorname,tutordob,tutorhours)
                    dbcursor.execute(SQL_statement,args)
                    print('INSERT statement executed successfully.') 
                    conn.commit()                                
                    dbcursor.close()              
                    conn.close() #Connection must be closed
                    return render_template('success.html', message='tutor record added')
                else:
                    print('DB connection Error')
                    return 'DB Connection Error'
            else:
                print('DB Connection Error')
                return 'DB Connection Error'
        else:
            print('Invalid tutor id received')
            return render_template('basicdbformexample.html')

@app.route('/update_tutor/', methods=['POST', 'GET'])
def update_tutor(): 
    #update tutor
    if request.method == 'GET':
        tutorid = request.args.get('tutors')
        print('Tutor id is: ', tutorid)
        if tutorid != None:
            conn = get_connection()          
            if conn != None:    #Checking if connection is None
                if conn.is_connected(): #Checking if connection is established
                    print('MySQL Connection is established')                          
                    dbcursor = conn.cursor()    #Creating cursor object            
                    SQL_statement = 'UPDATE TUTOR SET HOURS = 1 WHERE Tut_id = %s;'
                    args = (tutorid,)
                    dbcursor.execute(SQL_statement,args)                    
                    print('UPDATE statement executed successfully.')             
                    #rows = dbcursor.fetchall()                     
                    conn.commit()
                    dbcursor.close()              
                    conn.close() #Connection must be closed
                    return render_template('success.html', message='Tutor hours updated')
                else:
                    print('DB connection Error')
                    return 'DB Connection Error'
            else:
                print('DB Connection Error')
                return 'DB Connection Error'
        else:
            print('Invalid tutor id received')
            return render_template('basicdbformexample.html')
   
if __name__ == '__main__':
    app.run(debug = True)