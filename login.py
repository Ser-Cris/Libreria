from flask import Flask, session,request,Blueprint, render_template
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
    correo = encriptar(request.form.get('correo'))
    contraseña = encriptarContr(request.form.get('contrasena'))
    try:
        respuesta = mysqlconnector.Consulta_Usuarios(correo, contraseña)
        respuesta = respuesta.get_data(as_text=True)
        respuesta = json.loads(respuesta)
        usuario = respuesta['usuarios'][0]
        session['usuario'] = usuario[1]
        if usuario[3] != 'admin':
            return render_template('home_usuario.html', usuario=usuario[1])
        else:
            return render_template('home_admin.html', usuario=usuario[1])
            #return 'Sesión iniciada para el usuario: ' + session['usuario']
    except Exception as ex:
        print('No tas en la base de datos', ex)
        return render_template('login.html', booleano=False)

@rutas_login.route('/logout')
def logout():
    session.pop('usuario', None)
    return render_template('index.html', cerrarSesión=True)



