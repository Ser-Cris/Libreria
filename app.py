from flask import Flask,render_template,request
import mysqlconnector
import requests
import os

from login import rutas_login

def create_app():
    app = Flask(__name__)
    app.register_blueprint(rutas_login)
    app.secret_key = os.urandom(24)
    
    @app.route('/')
    def hello_world():
        respuesta =mysqlconnector.usuarios()
        print(respuesta.get_data(as_text=True))
        #mysqlconnector.Consulta_Usuarios()
        return render_template('index.html')
    @app.route('/login')
    def login():
        return render_template('login.html')

    return app
