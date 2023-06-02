from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('page.html')   

@app.route('/getInputs', methods=['GET', 'POST'])
def getInputs():
    if request.method == 'POST':
        username = request.form['username']
        numbers = []
        numbers.append(int(request.form['num1']))
        numbers.append(int(request.form['num2']))
        numbers.append(int(request.form['num3']))
        numbers.sort() 
        return render_template('outputPage.html', sortedNum = numbers, username = username ) 
    else:
        return redirect(url_for("index"))
    return redirect(url_for("index")) 


if __name__ == '__main__':
    for i in range(13000, 18000):
        try:
            app.run(debug = True, port = i)
            break
        except OSError as e:
            print("Port {} not available".format(i))