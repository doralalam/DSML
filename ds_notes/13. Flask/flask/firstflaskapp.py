'''
This code will explain how the Flask framework works using Python programming
'''

from flask import Flask

## WSGI Application
app = Flask(__name__) 
'''
This will create an instance of the Flask Class
Which will be our WSGI protocol for communication between web_server and web_application
We must assign the entry point for execution here
'''

## Decorator for home
@app.route('/')
## This decorator indicates it is a home page for the application
## If we enter '/' at the end of the generated URL, this message will be displayed in the web-page
def welcome():
    return "Welcome to the Flask Learning Environment!!! Feeling Excited!!! Let's Learn!!! How are you Feeling now???"



## Decorator for another page such as index
@app.route('/index')
## if we enter '/index' at end of the URL, a new web-page will be displayed with this message
def index():
    return "Welcome to the index page"



## Entry Point for execution
if __name__ == '__main__':
    ## To run the app
    app.run(debug=True)
    '''
    If we don't use debug option in run, we need to manually restart the application every time we make a change in the application
    This is a bad practice in real time application
    So, if we use debug=True, it will be automatically restared every time we save the changes and we can observe the change in output just by refreshing the web_page
    '''