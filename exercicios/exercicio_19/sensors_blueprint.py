#sensors.py
from flask import Blueprint, request, render_template, redirect, url_for

sensor = Blueprint("sensors", __name__, template_folder="templates")

sensors = {
    'umidade':'12',
    'luminosidade': '20',
    'temperatura':'24'
}

###################################################################################################
# @app.route('/sensors')
# def sensors():
        # dic = {'Umidade':22, 'Temperatura':23, 'Luminosidade':1034}
#     # sensores = ['Temperatura', 'Umidade', 'Luminosidade']
#     return render_template("sensors.html", devices=dic)

@sensor.route('/register_sensor')
def register_sensor():
    return render_template("register_sensor.html")

@sensor.route('/add_sensor', methods=['GET','POST'])
def add_sensors():
    global sensors
    if request.method == 'POST':
        name = request.form['sensor']
        number = request.form['number']
    else:
        name = request.args.get('sensor', None)
        number = request.args.get('number', None)
    sensors[name] = number
    return render_template("sensors.html", devices=sensors)

@sensor.route('/list_sensors')
def list_sensors():
    global sensors
    return render_template("sensors.html", devices=sensors)


@sensor.route('/remove_sensor')
def remove_sensor():
    return render_template("remove_sensor.html", devices=sensors)

@sensor.route('/del_sensor', methods=['GET','POST'])
def del_sensor():
    global sensors
    if request.method == 'POST':
        name = request.form['sensor']
    else:
        name = request.args.get('name', None)
    sensors.pop(name)
    return render_template("sensors.html", devices=sensors)