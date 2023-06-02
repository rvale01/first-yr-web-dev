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
    conn = get_connection()
    if conn != None:    #Checking if connection is None
        if conn.is_connected(): #Checking if connection is established
            print('MySQL Connection is established')                          
            dbcursor = conn.cursor()    #Creating cursor object            
            SQL_statement = 'SELECT Tut_id, TName from TUTOR;'            
            dbcursor.execute(SQL_statement)
            print('SELECT statement executed successfully.')             
            rows = dbcursor.fetchall()                                    
            dbcursor.close()              
            conn.close() #Connection must be closed
            return render_template('basicform.html', resultset=rows)
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
        tutorid = request.args.get('tutors')
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
            return render_template('basicdbform.html')  

if __name__ == '__main__':
    app.run(debug = True)