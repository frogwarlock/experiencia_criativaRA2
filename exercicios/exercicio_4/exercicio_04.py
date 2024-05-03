#app py
from flask import Flask, render_template


#objeto python
app = Flask(__name__)
##__name__ é o nome da aplicação

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/quarto')
def quarto():
    return render_template("quarto.html")

@app.route('/senslum')
def senslum():
    return render_template("senslum.html")

@app.route('/interruptor')
def interruptor():
    return render_template("interruptor.html")

@app.route('/banheiro')
def banheiro():
     return render_template("banheiro.html")

@app.route('/senshum')
def senshum():
    return render_template("senshum.html")

@app.route('/smartlight')
def smartlight():
    return render_template("smartlight.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)