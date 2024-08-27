
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, render_template
from connect import *

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/form', methods=['POST','GET'])
def registraForm():
    msg = ''
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        telefono = request.form['telefono']
        pais = request.form['pais']
        comida_favorita = request.form['comida_favorita']
        artista_favorito = request.form['artista_favorito']
        lugar_favorito = request.form['lugar_favorito']
        color_favorito = request.form['color_favorito']
        password = request.form['password']

        conexion_MySQLdb = connectionBD()
        cursor = conexion_MySQLdb.cursor(dictionary=True)

        sql = ("INSERT INTO Weplot (Nombre, Apellido, Email, Telefono, Pais, Comida_favorita, Artista_favorito, Lugar_favorito, Color_favorito, Password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        valores = (nombre, apellido, email, telefono, pais, comida_favorita, artista_favorito, lugar_favorito, color_favorito, password)

        cursor.execute(sql, valores)
        conexion_MySQLdb.commit()
        cursor.close()
        conexion_MySQLdb.close()
        msg = 'Registro con éxito'

        print("1 registro insertado ")

        return render_template('index.html', msg ='Formulario enviado')
    else:
        return render_template('index.html', msg ='Metodo HTTP incorrecto')



