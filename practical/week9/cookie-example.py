from flask import Flask, make_response, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('cookiemain.html')

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
   if request.method == 'POST':
	   user = request.form['nm']
	   resp = make_response(render_template('readcookie.html'))
	   resp.set_cookie('userID', user) 
	   # 3rd parameter can be max_age (in seconds) and if not specified 
	   # then cookie will cease to exist when the user closes the browser
	   # e.g., max_age=60*60*24*365*2   will set lifetime to 2 years
	   # a cookie can be deleted by calling set_cookie method and assing
	   # 0 to max_age
	   return resp
   else:
	   user = request.args.get('nm')
	   resp = make_response(render_template('readcookie.html'))
	   resp.set_cookie('userID', user)
	   return resp

@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('userID')
   return '<h1>welcome '+name+'</h1>'

if __name__ == '__main__':
   app.run(debug = True)
