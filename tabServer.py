from flask import Flask
from flask import render_template
import os
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/tab/<int:tab>/<string:dir>')
def tab_cmd(tab, dir):
    _ = os.popen(f"echo this is where to put command line for moving {tab} to {dir}").read()
    return f'move {tab} towards {dir}'