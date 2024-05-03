#app.py
#ADD CRIAR ARQUIVO SENSORS.PY PRA BLUEPRINT
from flask import Flask, render_template, jsonify, request, redirect, url_for
from login import login
from sensors_blueprint import sensor as sensorBp

sensores = {'Umidade':56, 'temperatura':26, 'luminosidade':1010}


app = Flask(__name__)
## __name__ is the application name

app.register_blueprint(login, url_prefix='/')
app.register_blueprint(sensorBp, url_prefix='/')



actuators = {
    'servo_motor',
    'lampada'
}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')




        
##################################################################################################
# @app.route('/actuators')
# def actuators():
#     return render_template("actuators.html", devices=actuators)

@app.route('/register_actuator')
def register_actuator():
    return render_template("register_actuators1.html")

@app.route('/add_actuator', methods=['GET','POST'])
def add_actuator():
    global actuators
    if request.method == 'POST':
        name = request.form['nome']
        actuators.add(name)
    else:
        name = request.args.get('nome', None)
        actuators[name]
    return render_template("actuators.html", devices=actuators)

@app.route('/list_actuators')
def list_actuators():
    global actuators
    return render_template("actuators.html", devices=actuators)

@app.route('/remove_actuator')
def remove_actuator():
    return render_template("remove_actuator.html", devices=actuators)

@app.route('/del_actuator', methods=['GET', 'POST'])
def del_actuator():
    global actuators
    if request.method == 'POST':
        name = request.form['atuadores']
        actuators.remove(name)
    elif request.method == 'GET':
        name = request.args.get('name', None)
        actuators.pop(name)
    return render_template("actuators.html", devices=actuators)




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)