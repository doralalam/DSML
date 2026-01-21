'''
This code demonstrates the practical use of Jinja2 Template Engine to pass {%...%} conditions

Jinja2 Template Engine is used to read the data from a data source and pass the value to the web_page

Multiple ways to access the variables using Jinja2 template engine:

{{   }}         expressions to print output in html
{%...%}         conditions, for loops etc
{#...#}         single line comments

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

## Variable Rule and Jinja2 Template Engine
## For loop example
@app.route('/successfor/<int:score>')
def successfor(score):
    res=""
    if score>=50:
        res= "PASSED"
    else:
        res= "FAILED"
    
    ## Passsing the value from Data source to the web_page
    dictionary = {'score':score, 'res':res}
    return render_template('resultFor.html',result=dictionary)

## If condition example
@app.route('/successif/<int:score>')
def successif(score):
    return render_template('resultIf.html', result=score)

if __name__ == '__main__':
    app.run(debug=True)