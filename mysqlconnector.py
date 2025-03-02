from flask import Flask, jsonify, request, Blueprint
from flaskext.mysql import MySQL
from login import desencriptar

app = Flask(__name__)




# Configuración de la base de datos MySQL
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'LibOnline'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'  # Asegúrate de que esta línea esté presente

mysql = MySQL()
mysql.init_app(app)

rutas_mysql = Blueprint('rutas_mysql', __name__)
@rutas_mysql.route('/Guardar_calificacion', methods=['GET'])
def Guardar_calificacion():
    try:
        ## id_usuario = request.args.get('id_usuario')
        ## id_libro = request.args.get('id_libro')

        conn = mysql.connect()
        cursor = conn.cursor()
        id_usuario = cursor.execute('SELECT id_usuario FROM Usuarios')
        id_libro = cursor.execute('SELECT id_libro FROM Libros')
        ranking = request.args.get('ranking')
        if ranking is None:
            return jsonify({"error": "Falta el parámetro ranking"}), 400

        if not id_usuario or not id_libro or not ranking:
            return jsonify({'error': 'Faltan datos'}), 400

        ranking = int(ranking)


        # Verificar si la calificación ya existe
        cursor.execute("SELECT * FROM Ranking WHERE id_usuario = %s AND id_libro = %s", (id_usuario, id_libro))
        calificacion_existente = cursor.fetchone()

        if calificacion_existente:
            nueva_suma_calificaciones = calificacion_existente[5] + ranking
            nueva_cantidad_calificaciones = calificacion_existente[4] + 1

            cursor.execute(
                "UPDATE Ranking SET ranking = %s, cantidad_calificaciones = %s, suma_calificaciones = %s WHERE id_usuario = %s AND id_libro = %s",
                (ranking, nueva_cantidad_calificaciones, nueva_suma_calificaciones, id_usuario, id_libro)
            )
        else:
            cursor.execute(
                "INSERT INTO Ranking (id_usuario, id_libro, ranking, cantidad_calificaciones, suma_calificaciones) VALUES (%s, %s, %s, %s, %s)",
                (id_usuario, id_libro, ranking, 1, ranking)
            )

        conn.commit()

        # Calcular el nuevo promedio
        cursor.execute("SELECT suma_calificaciones, cantidad_calificaciones FROM Ranking WHERE id_libro = %s",
                       (id_libro,))
        resultado = cursor.fetchone()

        if resultado:
            suma_calificaciones = resultado[0]
            cantidad_calificaciones = resultado[1]
            promedio = suma_calificaciones / cantidad_calificaciones

            data = {'promedio': promedio, 'mensaje': 'Calificación guardada exitosamente y promedio actualizado.'}
        else:
            data = {'mensaje': 'No se encontró el libro.'}

        conn.close()

        return jsonify(data)

    except Exception as ex:
        print(f"Error: {ex}")
        return jsonify({'mensaje': 'Error al guardar la calificación'}), 500


def consultaUn_Libro(id):
    data = {}
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM libros where id_libro = %s", (id,))
        libros = cursor.fetchall()
        data['libros'] = libros
        conn.close()
    except Exception as ex:
        data['mensaje'] = 'Error...'
    return jsonify(data)

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
        cursor.execute("SELECT id_usuario,nombre, apellidos, numero_telefonico FROM usuarios")
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
        correo = desencriptar(correo)
        cursor.execute(proc_alma,(correo,contrasena))
        print("yayirobe")
        usuario = cursor.fetchall()
        data['usuarios'] = usuario
        print(data['usuarios'][0][3])
        conn.close()
    except Exception as ex:
        print("Error en la consulta sql: ",ex)
        data['mensaje'] = 'Error...'
    return jsonify(data)
def Consulta_Direccion(id_usuario):
    data = {}
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        proc_alma = "CALL VerificarDireccionyUsuario(%s, %s)"
        cursor.execute(proc_alma,(id_usuario,id_usuario))
        dirNombre = cursor.fetchall()
        data['datos'] = dirNombre
        conn.close()
    except Exception as ex:
        print("Error en la consulta sql: ",ex)
        data['mensaje'] = 'Error...'
    return jsonify(data)
def Actualizar_Direccion(id_direccion,nombres,apellidos,num_telefonico,calle,num_interior,num_exterior,municipio,colonia,estado,cp):
    data = {}
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        #proc_alma = "CALL ActualizarDireccionyUsuario(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.callproc('ActualizarDireccionyUsuario',[id_direccion,nombres,apellidos,num_telefonico,calle,num_interior,num_exterior,municipio,colonia,estado,cp])
        conn.commit()
        dirNombre = cursor.fetchall()
        data['datos'] = dirNombre
        cursor.close()
        conn.close()
        data['estatus'] = True
    except Exception as ex:
        print("Error en la consulta sql: ", ex)
        data['estatus'] = False
    return jsonify(data)
