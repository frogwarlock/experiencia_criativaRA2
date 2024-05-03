#app.py
#ADD TELA METODO E ARQUIVO HTML PARA REMOVER ATUADORES
from flask import Flask, render_template, jsonify, request

sensores = {'Umidade':56, 'temperatura':26, 'luminosidade':1010}


app = Flask(__name__)
## __name__ is the application name



@app.route('/demonstration', methods=['GET'])
def demonstration():
    return jsonify(sensores)

users = {
    'user1': '1234',
    'user2': '1234'  
}

sensors = {
    'umidade':'12',
    'luminosidade': '20',
    'temperatura':'24'
}

actuators = {
    'servo_motor',
    'lampada'
}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/register_user')
def register_user():
    return render_template("register_user.html")

@app.route('/add_user', methods=['GET','POST'])
def add_user():
    global users
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
    else:
        user = request.args.get('user', None)
        password = request.args.get('password', None)
    users[user] = password
    return render_template("home.html", devices=users)

@app.route('/list_users')
def list_users():
    global users
    return render_template("users.html", devices=users)


@app.route('/validated_user', methods=['POST'])
def validated_user():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        print(user, password)
        if user in users and users[user] == password:
            return render_template('home.html')
        else:
            return '<h1> Invalid cretentials! </h1>'
    else:
        return render_template('login.html')

@app.route('/remove_user')
def remove_user():
    return render_template("remove_user.html", devices=users)
                           
@app.route('/del_user', methods=['GET','POST'])
def del_user():
    global users
    if request.method == 'POST':
        user = request.form['user']
    else:
        user = request.args.get('user', None)
    users.pop(user)
    return render_template("users.html", devices=users)

    

###################################################################################################
# @app.route('/sensors')
# def sensors():
        # dic = {'Umidade':22, 'Temperatura':23, 'Luminosidade':1034}
#     # sensores = ['Temperatura', 'Umidade', 'Luminosidade']
#     return render_template("sensors.html", devices=dic)

@app.route('/register_sensor')
def register_sensor():
    return render_template("register_sensor.html")

@app.route('/add_sensor', methods=['GET','POST'])
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

@app.route('/list_sensors')
def list_sensors():
    global sensors
    return render_template("sensors.html", devices=sensors)


@app.route('/remove_sensor')
def remove_sensor():
    return render_template("remove_sensor.html", devices=sensors)

@app.route('/del_sensor', methods=['GET','POST'])
def del_sensor():
    global sensors
    if request.method == 'POST':
        name = request.form['sensor']
    else:
        name = request.args.get('name', None)
    sensors.pop(name)
    return render_template("sensors.html", devices=sensors)
        

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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)