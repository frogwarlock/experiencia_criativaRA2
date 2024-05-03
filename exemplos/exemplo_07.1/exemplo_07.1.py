from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/sensors')
def sensors():
    dic = {'T1': 56, 'T2': 25, 'T3': 15}
    return render_template("sensors.html", devices=dic)

@app.route('/actuators')
def actuators():
    atuadores = {'ServoMotor': 90, 'Lâmpada': 0}
    # Adicionando uma variável de valor para demonstração
    value = 1
    return render_template("actuators.html", atuador=atuadores, value=value)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
