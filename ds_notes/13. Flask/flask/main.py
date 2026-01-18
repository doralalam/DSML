## To work on HTML page instead of a simple string message

from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    ## Returns the HTML output for root page
    return "<html><H1>Welcome to the Home page of Flask course !!!</H1></html>"

@app.route('/index')
def index():
    ## Returns the HTML output for index page
    return "<html><H1>This is the index page</H1></html>"

if __name__ == '__main__':
    app.run(debug=True)