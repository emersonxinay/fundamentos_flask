from flask import Flask, render_template
app = Flask(__name__)
# rutas
# @app.route('/')
# def index():
#     return "Hola amigos"

# segunda forma de poner rutas

def index2():
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
# bloque de pruebas
if __name__ == "__main__":
    app.add_url_rule('/', view_func=index2)
    # personalizando puertos y no reiniciar a cada rato el servidor
    app.run(debug=True, port=5005)

