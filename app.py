from flask import Flask, render_template, request
#from flask_mysqldb import MySQL

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/log')
def login():
	return render_template("log.html")

@app.route('/sign')
def signup():
	#if request.method == 'POST' :
		#userDetails = request.form 
		#name = userDetails['Name']
		#username = userDetails['Username']
		#password = userDetails['Password']
		#email = userDetails['Email'] 
	
	return render_template("sign.html")

if __name__ == "__main__":
	app.run(debug=True)