from flask import Flask, session

app = Flask(__name__)

app.secret_key = 'tu_clave_secreta'  # Necesario para usar sesiones


@app.route('/')
def index():
    session['usuario'] = 'nombre_de_usuario'
    return 'Sesión iniciada para el usuario: ' + session['usuario']


@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return 'Sesión cerrada'

if __name__ == '__main__':
    app.run(debug=True)

