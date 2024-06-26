#app.py
from flask import Flask, render_template, redirect, url_for, request
from login import login

app = Flask(__name__)
## __name__ is the application name

app.register_blueprint(login, url_prefix='/')

@app.route('/')
def index():
    return render_template('login.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)

