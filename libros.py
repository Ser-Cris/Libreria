from flask import Flask, session,request,Blueprint, render_template
import mysqlconnector
import json

rutas_libros = Blueprint('libros', __name__)

def Obtener_Libros():
    datos = mysqlconnector.consulta_Libros()
    datos = datos.get_data(as_text=True)
    datos = json.loads(datos)
    print(datos)
    return datos

@rutas_libros.route('/libros', methods=['GET', 'POST'])
def libros():
    datos = Obtener_Libros()
    print(datos)
    return datos