from flask import Flask,render_template,request,redirect,url_for
from flask_cors import CORS

app=Flask(__name__)
CORS(app) #inorder to avoid the cors restriction

#Home page of the bus tracking system
@app.route('/',methods=['POST','GET'])
def index():
    if request.method=='POST' and request.form['busno'] == "24": #the value returned will be a string
        return redirect(url_for('map'))
    else:
        return render_template('map.html')

#page for the map to show the moving bus and locations
@app.route('/map',methods=['POST','GET'])
def map():
    return render_template('route.html')


#page for the machine learning prediction of time
@app.route('/get_time',methods=['POST','GET'])
def get_time():
    return "10:00 Am"
if __name__=="__main__":
    app.run(debug=True)