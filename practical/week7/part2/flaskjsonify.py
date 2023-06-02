from flask import Flask, jsonify, json, render_template
app = Flask(__name__)

#let's assume CSCT data is in json format
data_csct = {    
    'zaheer' : 'WebDevelopment',
    'david'  : 'C++',
    'Kamran' : 'Front-end Development',
    'Shelan' : 'Machine Learning',
    'Barkha' : 'Databases',
    'students' : {
        '1001' : 'Andy Miller',
        '1002' : 'Amanda Joseph',
        '1003' : 'Bella Thorn',
        '1004' : 'Augusta Shine',
        '1005' : 'James Miller',
        '1006' : 'Mohammed Saleh'
    },
    'activites' : ["Open days", "Applicant days", "STEM", "Projects days"]
}
#creating seperate data objects
staff = {
    'zaheer' : 'WebDevelopment',
    'david'  : 'C++',
    'Kamran' : 'Front-end Development',
    'Shelan' : 'Machine Learning',
    'Barkha' : 'Databases'
}
#creating seperate data objects
students = {
    '1001' : 'Andy Miller',
    '1002' : 'Amanda Joseph',
    '1003' : 'Bella Thorn',
    '1004' : 'Augusta Shine',
    '1005' : 'James Miller',
    '1006' : 'Mohammed Saleh'
}
#creating seperate data objects
activites = ["Open days", "Applicant days", "STEM", "Projects days"]

@app.route('/')     
def index():
    return jsonify(data_csct)   #returns json data

@app.route('/index')     
def index_jsonify():
    return jsonify(staff=staff, students=students, activities=activites) 

@app.route('/data/')        #processed through jinja template
def data():
    data = json.dumps(data_csct)  #converting object to string 
    data = json.loads(data) #converting string to json object
    return(render_template('jsontemplate.html', data=data))

if __name__ == '__main__':
    app.run(debug = True)
    