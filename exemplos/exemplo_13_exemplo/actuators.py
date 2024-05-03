from flask import Blueprint, request, render_template, redirect, url_for

actuators = Blueprint("actuators",__name__, template_folder="templates")

actuatores ={'Servo': '0', 
            'Lampada': '1'}



# @app.route('/actuators')
# def actuators():
#     dic ={'Servo: ': 0, 'Lampada: ': 1}
#     #atuadores = ['servo motor', 'lampada']
#     return render_template("actuators.html", devices=dic)
@actuators.route('/register_actuator')
def register_actuator():
    return render_template("register_actuator.html")

@actuators.route('/add_actuator', methods=['GET','POST'])
def add_actuator():
    global actuatores
    if request.method == 'POST':
        actuator = request.form['actuator']
        number = request.form['number']
    else:
        actuator = request.args.get('actuator', None)
        number = request.args.get('number', None)
    actuatores[actuator] = number
    return render_template("actuators.html", devices=actuatores)

@actuators.route('/list_actuators')
def list_actuators():
    global actuatores
    return render_template("actuators.html", devices=actuatores)

@actuators.route('/remove_actuator')
def remove_actuator():
    return render_template("remove_actuator.html" , devices=actuatores)

@actuators.route('/del_actuator', methods=['GET','POST'])
def del_actuator():
    global actuatores
    if request.method == 'POST':
        actuator = request.form['actuator']
    else:
        actuator = request.args.get('actuator', None)
    actuators.pop(actuator)
    return render_template("actuators.html", devices=actuatores)

