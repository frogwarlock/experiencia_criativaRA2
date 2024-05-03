#app py
from flask import Flask


#objeto python
app = Flask(__name__)
##__name__ é o nome da aplicação

@app.route('/')
def index():
    return """
    <html>
        <head>Minha Casa</head>
        <body>
            <h2> Minha Casa </h2>
            <h3> Acesse o menu: </h3>
            <ul>
                <li><a href="/sensors"> Listar Sensores </a></li>
                <li><a href="/actuators"> Listar Atuadores </a></li>
            </ul>
        </body>
    </html>
"""

@app.route('/sensors')
def sensors():
    return """
    <html>
        <body>
            <h1> Sensores </h1>
            <ul>
                <li>Sensor de Umidade</li>
                <li>Sensor de Temperatura</li>
                <li>Sensor de Luminosidade</li>
            </ul>
            <p> Voltar para a <a href="/">página inicial</a>!</p>
        </body>
    </html>
"""

#EXERCICIO 1 FAZER A PAGINA HTML PARA OS ATUADORES
@app.route('/actuators')
def actuators():
    return """
    <html>
        <body>
            <h1> Atuadores </h1>
            <ul>
                <li>Servo Motor</li>
                <li>Lâmpada</li>
            </ul>
            <p> Voltar para a <a href="/">página inicial</a>!</p>
        </body>
    </html>
"""

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)