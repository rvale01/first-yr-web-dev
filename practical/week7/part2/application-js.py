from flask import Flask, render_template
app = Flask(__name__)

@app.route('/welcome/')
def index():
   return render_template('application-js.html')

if __name__ == '__main__':
   app.run(debug = True)
