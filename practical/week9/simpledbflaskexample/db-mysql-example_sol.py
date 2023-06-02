from flask import Flask, redirect, url_for, render_template, request
import dbfunc, mysql.connector
#import eventlet 

app = Flask(__name__)

  #Student Exercise with solution: 
      # T1: Can you spot data inconsistency when tutorstudentallocation updates student table?
         #Ans: Tutor table is not automatically updated and hence will have update anomaly 
      # T2: Think how are you going to update TUTOR table when tutorstudentallocation updates student table?
         #Ans: i) We are getting student ID so first we can use it to get who is current tutor or is it null 
         #    ii) Once we know who is current tutor we can update the tutor table for both current and new tutor 
         #    iii) We also need to check whether or not HOURS field is NULL 
      # T3: Can you implement solution you thought in T2?
         #Ans: see solution in tutorstudentallocation

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
            print(cursor)
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
         #conn.close()
      finally:       
         print('finally')  
         return render_template("result.html",msg = msg)
         #conn.close()
   else:
      print('Not POST')
      return 'Not POST'   
         

@app.route('/list')
def list():
   conn = dbfunc.getConnection()    
   cursor = conn.cursor()
   #cursor.execute("select s.SID, s.SNAME, s.EMAIL, t.TName from STUDENT s, TUTOR t WHERE s.Tutor_Id = t.Tut_Id ORDER BY SID")   
   cursor.execute("select s.SID, s.SNAME, s.EMAIL, t.TName from STUDENT s LEFT JOIN TUTOR t ON s.Tutor_Id = t.Tut_Id ORDER BY s.SID")   
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

      #Solution for T3 starts here
      #i. We check current Tutor ID
      cursor.execute('SELECT Tutor_Id FROM STUDENT WHERE SID = %s', (sid,))
      row = cursor.fetchall()
      current_tutor_id = row[0]    

      #. checking is current tutor id null or not 
      if current_tutor_id != None:
         print('A tutor already assigned')    
         # as it is not null, we reduce current tutor hours by 1 from tutor table
         update_tutor_query = "UPDATE TUTOR SET HOURS = (HOURS - 1) WHERE Tut_Id = %s"         
         cursor.execute(update_tutor_query, current_tutor_id)
         conn.commit()
         print('First if...')
      
      # we as it is not null, we reduce current tutor hours by 1 from tutor table
      cursor.execute('SELECT HOURS FROM TUTOR WHERE Tut_Id = %s', (tid,))
      row = cursor.fetchone()
      new_tutor_hours = row[0]      

      # checking if new tutor (who is assigned to a student) has any hours or is it null
      if new_tutor_hours != None:
         # if it is not null then use it as a number value
         new_tutor_hours = int(new_tutor_hours)
         print(new_tutor_hours)
         print('Second if...')
         #update hours for new tutor by adding 1, who is assigned to a student 
         update_tutor_query = "UPDATE TUTOR SET HOURS = (HOURS + 1) WHERE Tut_Id = %s"
         args = (tid, )
         cursor.execute(update_tutor_query, args)
         conn.commit()
         print('Tutor record updated')
      else:
         #this means tutor has no tutees and hours is NULL so we assign 1 to start
         print('A tutor is not assigned')  
         update_tutor_query = "UPDATE TUTOR SET HOURS = 1 WHERE Tut_Id = %s"
         args = (tid, )
         cursor.execute(update_tutor_query, args)
         conn.commit()
         print('Tutor record added')
      #Solution for iii ends here

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
