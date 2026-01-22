'''
This code demonstrates the practical use of Variable Rule
'''

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

'''
Variable Rule:
    Variable Rule is used to pass the parameters to the HTML page via URL
    By default the parameter passed is in string format
    Restricting a variable passing to the function to a particular data type using Flask framework by capturing the URL is known as Variable Rule

@app.route('/success/<score>')
def success(score):
    return 'Your score is '+ score
'''

## Here to mandate the variable to be of integer type
@app.route('/success/<int:score>')
def success(score):
    return 'Your score is '+ str(score)

if __name__ == '__main__':
    app.run(debug=True)