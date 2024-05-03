#app py
from flask import Flask, render_template


#objeto python
app = Flask(__name__)
##__name__ é o nome da aplicação

@app.route('/')
def index():
    comodos = ['quarto', 'banheiro']
    return render_template("index.html", spaces=comodos)

@app.route('/quarto')
def quarto():
    items = ['senslum', 'interruptor']
    return render_template("quarto.html", devices=items)

@app.route('/senslum')
def senslum():
    luminosidade = {'senslum':529}
    return render_template("senslum.html", lums = luminosidade)

@app.route('/interruptor')
def interruptor():
    interrup = {'interruptor':0}
    return render_template("interruptor.html", inter = interrup)

@app.route('/banheiro')
def banheiro():
    items = ['senshum', 'smartlight']
    return render_template("banheiro.html", devices=items)

@app.route('/senshum')
def senshum():
    umidade = {'SensorUmidade':27}
    return render_template("senshum.html", sensor=umidade)

@app.route('/smartlight')
def smartlight():
    luz = {'Luz':0}
    return render_template("smartlight.html", smartlight=luz)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)