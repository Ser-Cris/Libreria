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
def consulta_Libros():
    data = {}
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM libros")
        libros = cursor.fetchall()
        data['libros'] = libros
        conn.close()
    except Exception as ex:
        data['mensaje'] = 'Error...'
    return jsonify(data)
@app.route('/messi')
def usuarios():
    data = {}
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT nombre, apellidos, numero_telefonico FROM usuarios")
        usuarios = cursor.fetchall()
        data['usuarios'] = usuarios
        conn.close()
    except Exception as ex:
        data['mensaje'] = 'Error...'
    return jsonify(data)

@app.route('/cr7')
def Consulta_Usuarios(correo,contrasena):
    data = {}
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        proc_alma = "CALL VerificarUsuario(%s, %s)"
        cursor.execute(proc_alma,(correo,contrasena))
        print("yayirobe")
        usuario = cursor.fetchall()
        data['usuarios'] = usuario
        print(data['usuarios'][0][3])
        conn.close()
    except Exception as ex:
        data['mensaje'] = 'Error...'
    return jsonify(data)
