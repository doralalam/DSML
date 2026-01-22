'''
This code demonstrates how to build a URL dynamically
i.e., functions themselves redirect to another route based on the specified conditions and path instead of doing everything manually
'''

from flask import Flask, render_template, request, redirect, url_for
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

@app.route('/resultif/<int:score>')
def resultif(score):
    return render_template('resultIf.html', result=score)

@app.route('/scoresform', methods=['POST','GET'])
## form actions in HTML file use app.route() names to navigate among the methods
def scores():
    tot_score=0
    if request.method=='POST':
        DBMS=int(request.form['DBMS'])
        DS=int(request.form['DS'])
        tot_score = int(DBMS+DS)/2
        return redirect(url_for('resultif',score=tot_score))
    return render_template('scoresform.html')
'''
Above block explains that:
if the /getresult was entered via URL, then it is a GET request. So, go to the getresult.html file and execute it.
After entering the values in getresult.html file and submitting, it becomes a POST method, so then bring the values from the form and update the variables to validate the result using resultif function'''

if __name__=='__main__':
    app.run(debug=True)

'''
Note:   If we want to access the page by entering the path in URL, we must use GET method
        If we want to access the data from the server by passing the values, we must use POST method
        '''