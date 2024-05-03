# app.py
from flask import Flask, render_template, request
from login import login
from sensors import sensors
from actuators import actuators

app= Flask(__name__)
## __name__ is the application name

app.register_blueprint(login, url_prefix='/')
app.register_blueprint(sensors, url_prefix='/')
app.register_blueprint(actuators, url_prefix='/')


@app.route('/')
def index():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)

@app.route('/home')
def home():
    return render_template("home.html")








