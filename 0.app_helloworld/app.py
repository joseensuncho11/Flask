"""Ejercicio 1: Crear una aplicacion web basica con Flask que, al ser ejecutada, inicia un servidor local en el puerto 5000.
cuando visita la ruta principal (http://localhost:5000/),
el servidor respondera con mensaje HTML que dice "Hello, world Flask"."""

# Se importa el modulo Flask desde el paquete flask 
from flask import Flask

# Crear una instancia de la clase Flask.
# El argumento __name__ le dice a Flask 
# Que utilice el nombre del archivo actual main.py
app = Flask(__name__)

# Este es un decorador que define una ruta 
# corresponde a la pagina principal de app 
@app.route("/") 
# Cuando alguien visite app (por ejemplo, http://localhost:5000/),
# La funcion hello() sera ejecutada
def hello():
    return "<h1>Hello, World Flask !</h1>"

# Solo se ejecuta si el archivo es ejecutado directamente 
# Arranca la aplicacion Flask en modo de depuracion (debug=True),
if __name__ == '__main__':
    app.run(debug=True, port=5000)
 