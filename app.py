from flask import Flask,render_template,request
import mysqlconnector
import requests

from login import rutas_login
app = Flask(__name__)
app.register_blueprint(rutas_login)

@app.route('/')
def hello_world():
    respuesta =mysqlconnector.usuarios()
    print(respuesta.get_data(as_text=True))
    mysqlconnector.Consulta_Usuarios()
    return render_template('index.html')
@app.route('/login')
def login():
    return render_template('login.html')



if __name__ == '__main__':
    app.run(debug=True)