
from flask import Flask, render_template
app = Flask(__name__) 

studentsmarks = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60, 7:70, 8:80, 9:90, 10:100}
@app.route('/<int:studentId>')         
def getMark(studentId): 
    try: 
        result = ""
        grade = studentsmarks[studentId]
        if(grade>90):
            result = "A+"
        elif(grade>80 and grade<=90):
            result = "A"
        elif(grade>70 and grade<=80):
            result = "B+"
        elif(grade>60 and grade<=70):
            result = "B"
        elif(grade>50 and grade<=60):
            result = "C+"
        elif(grade>40 and grade<=50):
            result = "C"
        elif(grade>=35 and grade<=40):
            result = "C"
        elif(grade<35):
            result = "Resit"
    except(studentId>10 or studentId<1):
        result = "Wrong Id"
    return result


if __name__ == '__main__':    #you can skip this if running app on terminal window
    for i in range(13000, 18000):
      try:
         app.run(debug = True, port = i)
         break
      except OSError as e:
         print("Port {i} not available".format(i))