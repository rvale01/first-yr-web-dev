from flask import Flask, redirect, url_for, render_template, request
import dbfunc, mysql.connector
#import eventlet 

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home-flaskdemo.html')

@app.route('/enternew')
def new_student():
   return render_template('student.html')

@app.route('/addrec', methods = ['POST', 'GET'])
def addrec():
   msg = ""
   print('addrec')
   if request.method == 'POST':
      try:
         sid = request.form['sid']
         name = request.form['name']
         email = request.form['email']
         tutorid = None
         print('try')
         msg = sid + " " + name + " " + email 
         print(msg)
         conn = dbfunc.getConnection()
         if conn.is_connected():
            cursor = conn.cursor()
            sql_statement = "INSERT INTO STUDENT (SID, SNAME, EMAIL, Tutor_Id) \
            VALUES (%s, %s, %s, %s)"
            #print(cursor)
            args = (sid, name, email, tutorid)
            cursor.execute(sql_statement, args)
            conn.commit()
            cursor.close()
            msg += " - Record successfully added"
         print(msg)         
      except:
         print('except')
         conn.rollback()
         msg += " - error in insert operation"
         print(msg)         
      finally:       
         print('finally')  
         return render_template("result.html",msg = msg)         
   else:
      print('Not POST')
      return 'Not POST'   
      
@app.route('/list')
def list():
   conn = dbfunc.getConnection()    
   cursor = conn.cursor()    
   cursor.execute("select s.SID, s.SNAME, s.EMAIL, t.TName from STUDENT s LEFT \
      JOIN TUTOR t ON s.Tutor_Id = t.Tut_Id ORDER BY s.SID")   
   rows = cursor.fetchall() 
   return render_template("listrecords.html",rows = rows)

@app.route('/assigntutor')
def assigntutor():
   conn = dbfunc.getConnection()
   cursor = conn.cursor()
   cursor.execute("select * from STUDENT")   
   rows = cursor.fetchall()
   #print(rows)
   cursor.execute("select Tut_Id, TName, HOURS from TUTOR")   
   tutorrows = cursor.fetchall()
   return render_template("assigntutors.html",rows = rows, tutorrows=tutorrows)
        
@app.route('/tutorstudentallocation', methods = ['POST', 'GET'])
def tutorstudentallocation():
   if request.method == 'POST':
      sid = request.form['studentid']
      tid = request.form['tutorid']
      conn = dbfunc.getConnection()
      cursor = conn.cursor()
      sql_statement = "UPDATE STUDENT SET Tutor_Id = %s WHERE SID = %s"
      args = (tid, sid)
      print(args)
      cursor.execute(sql_statement, args)
      conn.commit()
      cursor.close()
      msg = "Record successfully updated"
      return render_template("result.html",msg = msg)
      
if __name__ == '__main__':
   app.run(debug=True)

#Student Exercise: Review db-mysql-example.py and run it on your computer. You'll need dbfunc
      # dbfunc with correct parameters (i.e. user name, password, database etc.)
      # T1: Can you spot data inconsistency when tutorstudentallocation updates student table?
      # T2: Think how are you going to update TUTOR table when tutorstudentallocation updates student table?
      # T3: Can you implement solution you thought in T2?