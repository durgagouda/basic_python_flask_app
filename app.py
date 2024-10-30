from flask import Flask
'''It Creates a instance of Flask class
which will be your WSGI(Web Server Gateway of Interface'''

### WSGI Application                      
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to Bangalore City"

@app.route("/index")
def index():
    return "Welcome to the index page"


if __name__ =="__main__":
    app.run(debug=True)