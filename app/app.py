from flask import Flask, render_template, request
app = Flask(__name__)
# rutas
# @app.route('/')
# def index():
#     return "Hola amigos"

# segunda forma de poner rutas

def index():
    data = {
        "titulo": "mi titulo",
        "encabezado": "Bienvenido"

    }
    return render_template("index.html", data = data)

# creando una ruta extra
@app.route('/holamundo')
def hola_mundo():
    return "Hola mundo de FLask"
# agregando ruta para contacto
@app.route('/contacto')
def contacto():
    data = {
        "titulo": "contacto",
        "encabezado": "Bienvenido"

    }
    return render_template("contacto.html", data = data)

# haciendo dinamico la web con login de prueb
@app.route('/saludo/<nombre>')
def saludando(nombre):
    # return 'Hola como estas '
    return f'hola, {nombre} como estas?'

# haciendo operación matematica
@app.route('/suma/<int:valor>/<int:valor2>')
def suma(valor, valor2):
    return f' la suma es: {valor+valor2}'

# para perfil con nombre y edad 
@app.route('/perfil/<nombre2>/<int:edad>')
def perfil(nombre2, edad):
    return f' mi nombre es {nombre2} y mi edad es {edad}'

# ruta para un diccionario de lenguajes de programación 
@app.route('/lenguajes')
def lenguajes():

    data= {
        'hay_lenguajes': True,
        'lenguajes': ['Ruby', 'Php', 'Python', 'Java', 'C#', 'Go', 'Dart', 'JavaScript']

    }
    
    return render_template('lenguajes.html', data=data)

# protocolos transfer  GET, POST, PUT, DELETE
@app.route('/datos')
def datos():
    # print(request.args)
    valor1 = request.args.get('valor1')
    return f"Solo son datos: {valor1} "

# bloque de pruebas
if __name__ == "__main__":
    app.add_url_rule('/', view_func=index)
    # personalizando puertos y no reiniciar a cada rato el servidor
    app.run(debug=True, port=5005)

