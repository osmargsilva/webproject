from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/")
def logim():
    return render_template('login.html')

@app.route('/register')
def cadastro():
    return render_template('register.html')

app.run(host="0.0.0.0", port=5001, debug=True)