from flask import Flask, session,request,Blueprint, render_template,request
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

@rutas_libros.route('/libros/<nombre_libro>')
def muestraUn_Libro(nombre_libro):
    id = request.args.get('id')
    print(id)
    datos = mysqlconnector.consultaUn_Libro(str(id))
    datos_par = datos.get_data(as_text=True)
    datos_par2 = json.loads(datos_par)
    libro = datos_par2["libros"][0]
    print(libro)
    return render_template("unLibro.html", libro=libro)