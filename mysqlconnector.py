from flask import Flask, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'LibOnline'

conexion = MySQL(app)

@app.route('/usuario')
def usuarios():
    data={}
    try:
        cursor=conexion.connection.cursor()
        sql="SELECT nombre, apellidos, numero_telefonico FROM usuarios"
        cursor.execute(sql)
        usuarios = cursor.fetchall()
        data['mensaje']='Éxito'
    except Exception as ex:
        data['mensaje']='Error...'
    return jsonify(data)


