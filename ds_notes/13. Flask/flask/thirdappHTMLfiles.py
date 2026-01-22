'''
This code explains how to redirect to the external HTML files using Flask Framework and render_template
'''
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    ## To redirect to the HTML file using Jinja2 Template engine
    return render_template('home.html')
    ## render_template will go and check for the templates folder for home.html file
    ## So, we need to create all the html files inside the templates folder

@app.route('/index')
def index():
       ## To redirect to the HTML file using Jinja2 Template engine
    return render_template('index.html')

@app.route('/about')
def about():
       ## To redirect to the HTML file using Jinja2 Template engine
    return render_template('about.html')


if __name__=='__main__':
    app.run(debug=True)