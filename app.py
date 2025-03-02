import json

from flask import Flask,render_template,request
import mysqlconnector
import requests
import os
from mysqlconnector import Guardar_calificacion
from mysqlconnector import rutas_mysql
from login import rutas_login
from libros import rutas_libros
from mysqlconnector import Consulta_Direccion
from login import session


def create_app():
    app = Flask(__name__)
    app.register_blueprint(rutas_login)
    app.register_blueprint(rutas_libros)
    app.register_blueprint(rutas_mysql)
    app.secret_key = os.urandom(24)
    @app.errorhandler(405)
    def method_not_allowed(e):
        return render_template('304.html'), 405
    @app.route('/')
    def hello_world():
        respuesta =mysqlconnector.usuarios()
        print(respuesta.get_data(as_text=True))
        #mysqlconnector.Consulta_Usuarios()
        return render_template('index.html')
    @app.route('/login')
    def login():
        return render_template('login.html')
    @app.route('/mi-perfil')
    def mi_perfil():
        data = Consulta_Direccion(session['id'])
        data = data.get_data(as_text=True)
        data = json.loads(data)
        print(data,type(data),sep="\n")
        return render_template('perfil.html',data=data)
    return app
