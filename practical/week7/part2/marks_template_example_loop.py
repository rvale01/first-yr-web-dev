from flask import Flask, render_template
app = Flask(__name__)

@app.route('/marks')
def result():
   dict = {'webprog':80, 'c prog':60, 'Java':70} 
   return render_template('loopexample.html', result = dict)

if __name__ == '__main__':
   app.run(debug = True)
