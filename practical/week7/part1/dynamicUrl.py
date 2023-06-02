from flask import Flask, redirect, url_for
import datetime
app = Flask(__name__) 

@app.route('/admin/<username>')
def admin(username):
    string = "welcome " + username+ " as Admin"
    return string

@app.route('/authorizedusers/<username>')
def authorizedusers(username):
    return "welcome " + username+ " as authorized user"

@app.route('/guests/<username>')
def guests(username):
    return "welcome " + username+ " as guest"

@app.route('/<username>') 
@app.route('/index/<username>')   
def index(username):
    ft = open("/Users/valentinaronchi/Desktop/school/uni/first year/web development/practical/week7/logs/logs.txt", "a")
    date = datetime.datetime.now()
    
    ft.write(date.strftime("%H:%M:%S") + " "+username +"\n" )
    ft.close()
    adminusers = ['zaheer.khan','kamran.soomro']
    authorizedusers =['david.wyatt','barkha.javed','shelan.jeawak'] 
    if username in adminusers:
        return redirect(url_for('admin', username =username))
    elif username in authorizedusers:
        return redirect(url_for('authorizedusers', username =username))
    else:
        return redirect(url_for('guests', username =username))



if __name__ == '__main__':    #you can skip this if running app on terminal window
    for i in range(13000, 18000):
      try:
         app.run(debug = True, port = i)
         break
      except OSError as e:
         print("Port {i} not available".format(i))