#app.py
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
def add_sensors():
    global users
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
    else:
        user = request.args.get('user', None)
        password = request.args.get('password', None)
    users[user] = password
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
    
@app.route('/list_users')
def list_users():
    global users
    return render_template("users.html", devices=users)

@app.route('/sensors')
def sensors():
    dic = {'Umidade':22, 'Temperatura':23, 'Luminosidade':1034}
    # sensores = ['Temperatura', 'Umidade', 'Luminosidade']
    return render_template("sensors.html", devices=dic)

@app.route('/actuators')
def actuators():
    atuadores = ['servo_motor', 'lampada']
    return render_template("actuators.html", atuador=atuadores)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)