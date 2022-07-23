from distutils.log import debug
from pip import main
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('welcome.html')

if "__name__" == main:
    app.run(debug=True)
    