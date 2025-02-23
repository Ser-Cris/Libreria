from flask import Flask, session,request,Blueprint, render_template
import mysqlconnector
import json
import os
import bcrypt
rutas_login = Blueprint('login', __name__)


 # Necesario para usar sesiones

@rutas_login.route('/enviar_datos',methods=['POST'])
def datitos():
    correo = request.form.get('correo')
    contraseña = request.form.get('contrasena')
    respuesta= mysqlconnector.Consulta_Usuarios(correo,contraseña)
    print(respuesta.get_data(as_text=True))
    return ("hola")
@rutas_login.route('/entra', methods=['POST'])
def index():
    correo = request.form.get('correo')
    contraseña = request.form.get('contrasena')
    correoEn = correo.encode('utf-8')
    contraseñaEn = contraseña.encode('utf-8')
    sal = b'$2b$12$Bj2s7PI42QkpqlbJtkAH/e'
    correo = str(bcrypt.hashpw(correoEn, sal))
    contraseña = str(bcrypt.hashpw(contraseñaEn, sal))
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
        print('No tas en la base de datos')
        return render_template('login.html', booleano=False)

@rutas_login.route('/logout')
def logout():
    session.pop('usuario', None)
    return render_template('index.html', cerrarSesión=True)



