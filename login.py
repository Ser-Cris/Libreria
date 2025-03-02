from flask import Flask, session, request, Blueprint, render_template
from cryptography.fernet import Fernet
import mysqlconnector
import json
import os
import bcrypt
rutas_login = Blueprint('login', __name__)


 # Necesario para usar sesiones

def encriptar(dato):
    key = b'MBM6KtJWagJf3dbl02QBqB4mblalri2noHfM9dss6YI='
    fernet = Fernet(key)
    datoEnc = fernet.encrypt(dato.encode('utf-8'))
    return datoEnc
def desencriptar(dato):
    key = b'MBM6KtJWagJf3dbl02QBqB4mblalri2noHfM9dss6YI='
    fernet = Fernet(key)
    datoDesenc = fernet.decrypt(dato).decode('utf-8')
    return datoDesenc
def encriptarContr(dato):
    sal = b'$2b$12$Bj2s7PI42QkpqlbJtkAH/e'
    datoEnc = dato.encode('utf8')
    Contra = str(bcrypt.hashpw(datoEnc, sal))
    return Contra
def compararContr(dato, hach):
    if bcrypt.checkpw(dato, hach):
        print("Que mirai vieja conchetumare")
        return True
    else:
        return False


@rutas_login.route('/enviar_datos',methods=['POST'])
def datitos():
    correo = request.form.get('correo')
    contraseña = request.form.get('contrasena')
    respuesta= mysqlconnector.Consulta_Usuarios(correo,contraseña)
    print(respuesta.get_data(as_text=True))
    return ("hola")
@rutas_login.route('/entra', methods=['POST'])
def index():
    if request.method == 'POST':
        correo = encriptar(request.form.get('correo'))
        contraseña = encriptarContr(request.form.get('contrasena'))
        try:
            respuesta = mysqlconnector.Consulta_Usuarios(correo, contraseña)
            respuesta = respuesta.get_data(as_text=True)
            respuesta = json.loads(respuesta)
            usuario = respuesta['usuarios'][0]
            session['usuario'] = usuario[1]
            session['id'] = usuario[0]
            if usuario[3] != 'admin':
                return render_template('home_usuario.html')
            else:
                return render_template('home_admin.html', usuario=usuario[1])
                #return 'Sesión iniciada para el usuario: ' + session['usuario']
        except Exception as ex:
            print('No tas en la base de datos', ex)
@rutas_login.route('/actualizar', methods=['POST'])
def actualizar():
    if request.method == "POST":
        nombres = request.form.get('nombres')
        apellidos = request.form.get('apellidos')
        num_telefonico = request.form.get('num_telefonico')
        calle = request.form.get('calle')
        num_interior = request.form.get('num_interior')
        num_exterior = request.form.get('num_exterior')
        municipio = request.form.get('municipio')
        colonia = request.form.get('colonia')
        estado = request.form.get('estado')
        cp = request.form.get('cp')
        print(nombres,apellidos,num_telefonico,calle,num_interior,num_exterior,municipio,colonia,estado,cp, sep="\t")
        try:
            respuesta = mysqlconnector.Actualizar_Direccion(session['id'],nombres, apellidos, num_telefonico, calle, num_interior, num_exterior, municipio, colonia, estado, cp)
            respuesta = respuesta.get_data(as_text=True)
            respuesta = json.loads(respuesta)
            if respuesta['estatus'] == True:
                return render_template('success_actu.html')
            else:
                return render_template('error_actu.html')
        except:
            print("No se ha podido actualizar")
            return render_template("perfil.html")
@rutas_login.route('/logout')
def logout():
    session.pop('usuario', None)
    return render_template('index.html', cerrarSesión=True)



