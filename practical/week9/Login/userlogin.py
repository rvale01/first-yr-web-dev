import mysql.connector
from flask import Flask, render_template, request, session, redirect, url_for
from passlib.hash import sha256_crypt
import hashlib
import gc
from functools import wraps

#example adapted from:
#https://pythonprogramming.net/flask-registration-tutorial/?completed=/flask-user-registration-form-tutorial/
app = Flask(__name__)
app.secret_key = 'This is my Secret Key'     #secret keey for sessions

#establishing a database connectoion. You may use dbfunc.py here. 
def get_connection():                       
    conn = mysql.connector.connect(host='localhost',                     
                              user='valentina2ronchi',
                              password='Valentina2ronchI16+$++',
                              port='3307',
                              database='STUDENTSREG')
    return conn

# / or /index creates a route that loads the main page where 
# register and login options are offered to end users
@app.route('/')
@app.route('/index/')
def mainpage_override():
    return render_template('mainpage.html')

# /index/<usertype> creates an end point that should display contents on 
# mainpage.html based on user type e.g., if user type is admin then 
# show adminfeatures, or if user type is standard then show standard 
# user feastures
@app.route('/index/<usertype>')
def mainpage(usertype):
    return render_template('mainpage.html', usertype=usertype)

# Now we create a route that registers a user account. 
# It gets post method request with suggested user name and password. 
# If user name and password are legit data items, the method will get 
# connection, generate password hash, check database to verify if the 
# same user name already exists in the database. Starts the registration proces
# again if user already exists. Otherwise, user account details with 
# hashed password are stored. 
# Password is hashed before storing in the database.

#/register/ route registers a new user. By default user type is standard.
@app.route('/register/', methods=['POST', 'GET'])
def register():
    error = ''
    print('Register start')
    try:
        if request.method == "POST":         
            username = request.form['username']
            password = request.form['password']
            email = request.form['email']                      
            if username != None and password != None and email != None:           
                conn = get_connection()
                if conn != None:    #Checking if connection is None           
                    if conn.is_connected(): #Checking if connection is established
                        print('MySQL Connection is established')                          
                        dbcursor = conn.cursor()    #Creating cursor object 
                        #here we should check if username / email already exists                                                           
                        password = sha256_crypt.hash((str(password)))           
                        Verify_Query = "SELECT * FROM users WHERE username = %s;"
                        dbcursor.execute(Verify_Query,(username,))
                        rows = dbcursor.fetchall()           
                        if dbcursor.rowcount > 0:   #this means there is a user with same name
                            print('username already taken, please choose another')
                            error = "User name already taken, please choose another"
                            return render_template("register.html", error=error)    
                        else:   #this means we can add new user             
                            dbcursor.execute("INSERT INTO users (username, password_hash, \
                                 email) VALUES (%s, %s, %s)", (username, password, email))                
                            conn.commit()  #saves data in database              
                            print("Thanks for registering!")
                            dbcursor.close()
                            conn.close()
                            gc.collect()                        
                            session['logged_in'] = True     #session variables
                            session['username'] = username
                            session['usertype'] = 'standard'   #default all users are standard
                            return render_template("success.html",\
                             message='User registered successfully and logged in..')
                    else:                        
                        print('Connection error')
                        return 'DB Connection Error'
                else:                    
                    print('Connection error')
                    return 'DB Connection Error'
            else:                
                print('empty parameters')
                return render_template("register.html", error=error)
        else:            
            return render_template("register.html", error=error)        
    except Exception as e:                
        return render_template("register.html", error=e)    
    return render_template("register.html", error=error)

#/login/ route receives user name and password and checks against db user/pw
@app.route('/login/', methods=["GET","POST"])
def login():
    form={}
    error = ''
    try:	
        if request.method == "POST":            
            username = request.form['username']
            password = request.form['password']            
            form = request.form
            print('login start 1.1')
            
            if username != None and password != None:  #check if un or pw is none   
                print(username, password, 'checking logs')       
                conn = get_connection()
                if conn != None:    #Checking if connection is None                    
                    if conn.is_connected(): #Checking if connection is established                        
                        print('MySQL Connection is established')                          
                        dbcursor = conn.cursor()    #Creating cursor object                                                 
                        dbcursor.execute("SELECT password_hash, usertype \
                            FROM users WHERE username = %s;", (username,))                                                
                        data = dbcursor.fetchone()
                        #print(data[0])
                        if dbcursor.rowcount < 1: #this mean no user exists                         
                            error = "User / password does not exist, login again"
                            return render_template("login.html", error=error)
                        else:                            
                            #data = dbcursor.fetchone()[0] #extracting password   
                            # verify passowrd hash and password received from user                                                             
                            if sha256_crypt.verify(request.form['password'], str(data[0])):                                
                                session['logged_in'] = True     #set session variables
                                session['username'] = request.form['username']
                                session['usertype'] = str(data[1])                          
                                print("You are now logged in")                                
                                # return render_template('userresources.html', \
                                #     username=username, data='this is user specific data',\
                                #          usertype=session['usertype'])
                            else:
                                error = "Invalid credentials username/password, try again."                               
                    gc.collect()
                    print('login start 1.10')
                    return render_template("login.html", form=form, error=error)
    except Exception as e:                
        error = str(e) + " <br/> Invalid credentials, try again."
        return render_template("login.html", form=form, error = error)   
    
    return render_template("login.html", form=form, error = error)
            
#https://pythonprogramming.net/decorator-wrappers-flask-tutorial-login-required/?completed=/flask-user-log-in-system-tutorial/
#Now that we can have users register and log in, we're also allowing them 
# to log out. It makes a little sense to not let users log out, unless 
# they are logged in! Here, we define the function, where the parameter is f, 
# which is convention for the fact that it wraps a function. Then, we define 
# the wrapper. 
# #Our wrapper here is simple, it just simply checks if the user 
# has a "logged_in" in their session. If so, great. If not, they should get   
# a message and a redirect to the login page.
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:            
            print("You need to login first")
            #return redirect(url_for('login', error='You need to login first'))
            return render_template('login.html', error='You need to login first')    
    return wrap

#We also write a wrapper for admin user(s). It will check with the user is 
# logged in and the usertype is admin and only then it will allow user to
# perform admin functions
def admin_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if ('logged_in' in session) and (session['usertype'] == 'admin'):
            return f(*args, **kwargs)
        else:            
            print("You need to login first as admin user")
            #return redirect(url_for('login', error='You need to login first as admin user'))
            return render_template('login.html', error='You need to login first as admin user')    
    return wrap

#We also write a wrapper for standard user(s). It will check with the usertype is 
#standard and user is logged in, only then it will allow user to perform standard user functions
def standard_user_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if ('logged_in' in session) and (session['usertype'] == 'standard'):
            return f(*args, **kwargs)
        else:            
            print("You need to login first as standard user")
            #return redirect(url_for('login', error='You need to login first as standard user'))
            return render_template('login.html', error='You need to login first as standard user')    
    return wrap

#/logout is to log out of the system.
# Here we us @login_required wrapper ... this means that a user can only 
# log out if that user is logged in
@app.route("/logout/")
@login_required
def logout():    
    session.clear()    #clears session variables
    print("You have been logged out!")
    gc.collect()
    return render_template('mainpage.html', optionalmessage='You have been logged out')

#/userfeatures is loaded for standard users
# Here we us @standard_user_login_required wrapper ... 
# this means that only users with user type standard can access this function
# the function implements features related to standard users
@app.route('/userfeatures/')
@login_required
@standard_user_required
def user_features():
        print('fetchrecords')
        #records from database can be derived
        #user login can be checked..
        print ('Welcome ', session['username'])
        return render_template('standarduser.html', \
            user=session['username'], message='User data from app and standard \
                user features can go here....')

#/adminfeatures is loaded for admin users
# Here we us @admin_required wrapper ... 
# this means that only users with user type admin can access this function
# the function implements features related to admin users
@app.route('/adminfeatures/')
@login_required
@admin_required
def admin_features():
        print('create / amend records / delete records / generate reports')
        #records from database can be derived, updated, added, deleted
        #user login can be checked..
        print ('Welcome ', session['username'], ' as ', session['usertype'])
        return render_template('adminuser.html', user=session['username'],\
             message='Admin data from app and admin features can go here ...')

#/generateadminreport is loaded for admin users only
# Here we us @admin_required wrapper ... 
# this means that only users with user type admin can access this function
# the function implements features related to admin users
@app.route('/generateadminreport/')
@login_required
@admin_required
def generate_admin_report():
    print('admin reports')
    #here you can generate required data as per business logic
    return """
        <h1> this is admin report for {} </h1>
        <a href='/adminfeatures')> Go to Admin Features page </a>
    """.format(session['username'])

#/generateuserrecord is loaded for standard users only
# Here we us @standard_user_required wrapper ... 
# this means that only users with user type standard can access this function
# the function implements features related to standard users
@app.route('/generateuserrecord/')
@login_required
@standard_user_required
def generate_user_record():
    print('User records')
    #here you can generate required data as per business logic
    return """
        <h1> this is User record for user {} </h1>
        <a href='/userfeatures')> Go to User Features page </a>
    """.format(session['username'])
    

if __name__ == '__main__':
    for i in range(13000, 18000):
        try:
            app.run(debug = True, port = i)
            break
        except OSError as e:
            print("Port {} not available".format(i))
