from flask import Flask, render_template
app = Flask(__name__) 


@app.route('/')         #Decorator / route / View
def index():            #function associated with the decorator
   print ('Hello')      #output on server side only (good for debugging)
   return render_template('CSSinternalDiv.html')

if __name__ == '__main__':    #you can skip this if running app on terminal window
    for i in range(13000, 18000):
      try:
         app.run(debug = True, port = i)
         break
      except OSError as e:
         print("Port {i} not available".format(i))