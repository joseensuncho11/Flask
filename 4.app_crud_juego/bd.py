"""
CRUD FLASK PYTHON + MYSQL
Desarrollado por: Jose Daniel Ensuncho Benitez
"""

# Realizamos la importación de la librería con pip install PyMySQL
import pymysql

# Configuramos los datos de conexión con la base de datos
def obtener_conexion():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='daniel',
        db='app_crud_juego'
    )
