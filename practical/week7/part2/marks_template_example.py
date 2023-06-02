from flask import Flask, render_template
app = Flask(__name__) 

@app.route('/marks/<int:score>')
def hello_name(score):
    return render_template('ifexample.html', marks = score)

if __name__ == '__main__':
    app.run(debug = True)
