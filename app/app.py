from flask import Flask
app = Flask(__name__)
# rutas
# @app.route('/')
# def index():
#     return "Hola amigos"

# segunda forma de poner rutas

def index2():
    return "hola de segunda forma estamos mejor"

# creando una ruta extra
@app.route('/holamundo')
def hola_mundo():
    return "Hola mundo de FLask"
# bloque de pruebas
if __name__ == "__main__":
    app.add_url_rule('/', view_func=index2)
    # personalizando puertos y no reiniciar a cada rato el servidor
    app.run(debug=True, port=5005)
