#app py
from flask import Flask


#objeto python
app = Flask(__name__)
##__name__ é o nome da aplicação

@app.route('/')
def index():
    return """
    <html>
        <head>Casa</head>
        <body>
            <h2> Minha Casa </h2>
            <h3> Acesse o menu: </h3>
            <ul>
                <li><a href="/quarto"> Quarto </a></li>
                <li><a href="/banheiro"> Banheiro </a></li>
            </ul>
        </body>
    </html>
"""

@app.route('/quarto')
def quarto():
    return """
    <html>
        <body>
            <h1> Quarto </h1>
            <ul>
                <li><a href="/senslum"> Sensor de Luminosidade </a></li>
                <li><a href="/interruptor"> Interruptor </a></li>
            </ul>
            <p> Voltar para a <a href="/">página inicial</a>!</p>
        </body>
    </html>
"""

@app.route('/senslum')
def senslum():
    return """
    <html>
        <body>
            <h1> Sensor Luminosidade </h1>
            <ul>
                <li>Sensor de Luminosidade</li>
            </ul>
            <p> Voltar para a <a href="/">página inicial</a>!</p>
        </body>
    </html>
"""
@app.route('/interruptor')
def interruptor():
    return """
    <html>
        <body>
            <h1>Interruptor </h1>
            <ul>
                <li>Interruptor</li>
            </ul>
            <p> Voltar para a <a href="/">página inicial</a>!</p>
        </body>
    </html>
"""

@app.route('/banheiro')
def banheiro():
     return """
    <html>
        <body>
            <h1> Banheiro </h1>
            <ul>
                <li><a href="/senshum"> Sensor de Umidade </a></li>
                <li><a href="/smartlight"> Lâmpada Inteligente </a></li>
            </ul>
            <p> Voltar para a <a href="/">página inicial</a>!</p>
        </body>
    </html>
"""

@app.route('/senshum')
def senshum():
    return """
    <html>
        <body>
            <h1>Sensor de Umidade </h1>
            <ul>
                <li>Sensor de umidade</li>
            </ul>
            <p> Voltar para a <a href="/">página inicial</a>!</p>
        </body>
    </html>
"""

@app.route('/smartlight')
def smartlight():
    return """
    <html>
        <body>
            <h1>Lâmpada Inteligente </h1>
            <ul>
                <li>Lâmpada Inteligente</li>
            </ul>
            <p> Voltar para a <a href="/">página inicial</a>!</p>
        </body>
    </html>
"""

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)