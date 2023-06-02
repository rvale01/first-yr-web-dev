from flask import Flask, render_template
app = Flask(__name__) 


@app.route('/<name>')         #Decorator / route / View
def getName(name):            #function associated with the decorator
   print ('Hello')      #output on server side only (good for debugging)
   return render_template('./UWEPage.html', user = name)

if __name__ == '__main__':    #you can skip this if running app on terminal window
    for i in range(13000, 18000):
      try:
         app.run(debug = True, port = i)
         break
      except OSError as e:
         print("Port {i} not available".format(i))