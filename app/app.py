from flask import Flask
app = Flask(__name__)
# rutas
@app.route('/')
def index():
    return "Hola amigos"

# bloque de pruebas
if __name__ == "__main__":
    
    app.run()
