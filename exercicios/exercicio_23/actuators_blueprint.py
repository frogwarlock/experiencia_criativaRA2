#actuators.py
from flask import Blueprint, request, render_template, redirect, url_for

actuator = Blueprint("actuators", __name__, template_folder="templates")

actuators = {
    'servo_motor',
    'lampada'
}

##################################################################################################
# @app.route('/actuators')
# def actuators():
#     return render_template("actuators.html", devices=actuators)

@actuator.route('/register_actuator')
def register_actuator():
    return render_template("register_actuators1.html")

@actuator.route('/add_actuator', methods=['GET','POST'])
def add_actuator():
    global actuators
    if request.method == 'POST':
        name = request.form['nome']
        actuators.add(name)
    else:
        name = request.args.get('nome', None)
        actuators[name]
    return render_template("actuators.html", devices=actuators)

@actuator.route('/list_actuators')
def list_actuators():
    global actuators
    return render_template("actuators.html", devices=actuators)

@actuator.route('/remove_actuator')
def remove_actuator():
    return render_template("remove_actuator.html", devices=actuators)

@actuator.route('/del_actuator', methods=['GET', 'POST'])
def del_actuator():
    global actuators
    if request.method == 'POST':
        name = request.form['atuadores']
        actuators.remove(name)
    elif request.method == 'GET':
        name = request.args.get('name', None)
        if name in actuators:
            actuators.remove(name)
    return render_template("actuators.html", devices=actuators)

