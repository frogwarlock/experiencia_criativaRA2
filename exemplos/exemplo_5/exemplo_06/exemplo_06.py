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
    sensores = ['Temperatura', 'Umidade', 'Luminosidade']
    return render_template("sensors.html", devices=sensores)

#EXERCICIO 5
@app.route('/actuators')
def actuators():
    atuadores = ['servo_motor', 'lampada']
    return render_template("actuators.html", atuador=atuadores)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)