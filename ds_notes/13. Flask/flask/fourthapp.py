'''
This code will explain how the GET and POST methods work and
uses home.html, index.html, form.html files from the templates folder
'''

## To import Flask framework
from flask import Flask
## To redirect to HTML page
from flask import render_template
## To handle the http requests
from flask import request

## To create an object for Flask
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/index', methods=['GET'])
## Even though, we didn't set the methods attribute, by default it is set to GET
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

'''
    Here, we used both GET and POST methods
    GET is used for simple retreival
    POST sends the data to server and then retrieves the information
'''
    
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        ## To get the name value from the form
        name=request.form['name']
        ## To display a message with name from the form
        return f"Hello {name}"
    return render_template('form.html')
'''
if we stop at the above code, after submitting the form, it will return Hello {name} but it is still in form page only
to redirect the output from form page to submit page
'''

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name=request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')


if __name__=='__main__':
    ## To run the flask object
    app.run(debug=True)

'''
The main difference between GET and POST method is:

GET: Used to retreive the information without passing any parameter to search
        Example: A simple Google Home page where we don't pass any input to search

POST: Used to retrieve the information by passing a value to search
        Example: If we search for a dog in Google, we will pass Dog argument in the search bar which will be used to query the result

        
Purpose and Safety:

    GET fetches resources without side effects, ensuring repeated calls yield the same result.

    POST sends data to create or update resources, intentionally changing server state like form submissions.

Data Transmission:

    GET appends parameters to the URL as query strings, limiting payload size (~2KB max) and exposing data visibly.

    POST places data in the request body, supporting larger payloads including files and binary data securely.

Visibility and Caching:

    GET URLs appear in browser history, logs, and bookmarks; responses cache easily for faster retrieval.

    POST data stays hidden from URLs, preventing caching or bookmarking to protect sensitive information
'''