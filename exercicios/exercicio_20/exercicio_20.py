#app.py
#ADD CRIAR ARQUIVO ACTUATORS.PY PRA BLUEPRINT
from flask import Flask, render_template, jsonify, request, redirect, url_for
from login import login
from sensors_blueprint import sensor as sensorBp
from actuators_blueprint import actuator as actuatorBp

app = Flask(__name__)
## __name__ is the application name

app.register_blueprint(login, url_prefix='/')
app.register_blueprint(sensorBp, url_prefix='/')
app.register_blueprint(actuatorBp, url_prefix='/')


@app.route('/')
def index():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)