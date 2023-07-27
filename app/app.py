from flask import Flask
app = Flask(__name__)
# rutas
# @app.route('/')
# def index():
#     return "Hola amigos"

# segunda forma de poner rutas

def index2():
    return "hola de segunda forma"

# bloque de pruebas
if __name__ == "__main__":
    app.add_url_rule('/', view_func=index2)
    
    app.run()
