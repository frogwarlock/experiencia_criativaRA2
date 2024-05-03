#app py
from flask import Flask, render_template


#objeto python
app = Flask(__name__)
##__name__ é o nome da aplicação

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/sensors')
def sensors():
    dic = {'Umidade':22, 'Temperatura':23, 'Luminosidade':1034}
    # sensores = ['Temperatura', 'Umidade', 'Luminosidade']
    return render_template("sensors.html", devices=dic)

@app.route('/actuators')
def actuators():
    atuadores = {'Servo':122, 'Lâmpada':1}
    # atuadores = ['servo_motor', 'lampada']
    return render_template("actuators.html", atuador=atuadores)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)