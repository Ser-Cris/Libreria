from flask import Flask, jsonify
from flaskext.mysql import MySQL

app = Flask(__name__)

# Configuración de la base de datos MySQL
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'LibOnline'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'  # Asegúrate de que esta línea esté presente

mysql = MySQL()
mysql.init_app(app)

@app.route('/messi')
def usuarios():
    data = {}
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT nombre, apellidos, numero_telefonico FROM usuarios")
        usuarios = cursor.fetchall()
        data['usuarios'] = usuarios
    except Exception as ex:
        data['mensaje'] = 'Error...'
    return jsonify(data)

