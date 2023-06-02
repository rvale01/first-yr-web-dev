from flask import Flask, render_template, json, jsonify
app = Flask(__name__) 

data_csct = {
 'zaheer' : 'WebDevelopment',
 'david' : 'C++',
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
#creating seperate data dictionary for staff
staff = {
 'zaheer' : 'WebDevelopment',
 'david' : 'C++',
 'Kamran' : 'Front-end Development',
 'Shelan' : 'Machine Learning',
 'Barkha' : 'Databases'
}
#creating seperate data dictionary for students
students = {
 '1001' : 'Andy Miller',
 '1002' : 'Amanda Joseph',
 '1003' : 'Bella Thorn',
 '1004' : 'Augusta Shine',
 '1005' : 'James Miller',
 '1006' : 'Mohammed Saleh'
}
#creating seperate data list for activities
activites = ["Open days", "Applicant days", "STEM", "Projects days"]


@app.route('/task1')         
def taskOne(): 
   return jsonify(data_csct)

@app.route('/task2')         
def taskTwo(): 
    return jsonify(staff=staff, students = students, activities = activites)

@app.route('/task3')         
def taskThree(): 
    data = json.dumps(data_csct)
    data = json.loads(data)
    return data

@app.route('/task4')         
def taskFour(): 
    data = json.dumps(data_csct)
    data = json.loads(data)
    string = ""
    for item in data['students']:
        string = string + item + ": " + data['students'][item] + "<br>"

    return string

@app.route('/<studId>')      
def taskFive(studId):
    data = json.dumps(data_csct)
    data = json.loads(data)
    string = "Student not found"
    for item in data['students']:
        if(studId = item):
            string = item + ": " + data['students'][item]
            break

    return string


if __name__ == '__main__':    #you can skip this if running app on terminal window
    for i in range(13000, 18000):
      try:
         app.run(debug = True, port = i)
         break
      except OSError as e:
         print("Port {i} not available".format(i))