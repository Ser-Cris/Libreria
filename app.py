from flask import Flask,render_template
import mysqlconnector
import requests
app = Flask(__name__)

@app.route('/')
def hello_world():
    respuesta =mysqlconnector.usuarios()
    print(respuesta.get_data(as_text=True))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)