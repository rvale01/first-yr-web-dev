from flask import Flask, request, render_template, url_for, jsonify
app = Flask(__name__)

#This can be from your database. For demonstration, I am using dictionary
routes = {
			'Newcastle' : ['Bristol'],
			'Bristol' : ['Newcastle', 'New York', 'Manchester', 'Glasgow', 'Mainhead'],
			'Cardiff' : ['Edinburgh'],
			'Manchester' : ['Bristol', 'Birmingham', 'Glasgow', 'Southampton'],
			'London' : ['Manchester'],
			'Birmingham' : ['Newcastle'],
			'Edinburgh' : ['Cardiff']
		}

@app.route('/')
def index():
		depaturecities = routes.keys()  
		return render_template('citiesform.html', departurelist=depaturecities)   

@app.route ('/returncity/', methods = ['POST', 'GET'])
def ajax_returncity():   
	print('/returncity') 
	if request.method == 'GET':
		q = request.args.get('q')    
		returncities = routes[q]
		total = len(returncities)
		print(returncities)
		print(total)
		return jsonify(returncities=returncities, size=total)
	else:
		print('Error')
		return jsonify(returncities='error')

@app.route ('/dumpsVar/', methods = ['POST', 'GET'])
def dumpVar():
    if request.method == 'POST':
        result = request.form
        output = "<H2>Data Received: </H2></br>"
        output += "Number of Data Fields : " + str(len(result))
        for key in list(result.keys()):
            output = output + " </br> " + key + " : " + result.get(key)
        return output
    else:
        result = request.args
        output = "<H2>Data Received: </H2></br>"
        output += "Number of Data Fields : " + str(len(result))
        for key in list(result.keys()):
            output = output + " </br> " + key + " : " + result.get(key)
        return output  

if __name__ == '__main__':
   app.run (debug = True)


