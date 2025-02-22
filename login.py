from flask import Flask, session,request,Blueprint
import mysqlconnector
rutas_login = Blueprint('login', __name__)


rutas_login.secret_key = 'tu_clave_secreta'  # Necesario para usar sesiones

@rutas_login.route('/enviar_datos',methods=['POST'])
def datitos():
    correo = request.form.get('correo')
    contraseña = request.form.get('contrasena')
    respuesta= mysqlconnector.Consulta_Usuarios(correo,contraseña)
    print(respuesta.get_data(as_text=True))
    return ("hola")
@rutas_login.route('/entra')
def index():
    session['usuario'] = 'nombre_de_usuario'
    return 'Sesión iniciada para el usuario: ' + session['usuario']


@rutas_login.route('/logout')
def logout():
    session.pop('usuario', None)
    return 'Sesión cerrada'



