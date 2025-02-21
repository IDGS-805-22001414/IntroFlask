
from datetime import datetime
from forms import ZodiacoForm
from flask import Flask, render_template, request, redirect, url_for
import forms
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, RadioField, SubmitField
from wtforms.validators import DataRequired, NumberRange
from flask import g
from flask_wtf.csrf import CSRFProtect

from datetime import date
from flask import Flask
from flask import flash 
import forms 


app = Flask(__name__)
app.secret_key= 'alonMtz'
csrf=CSRFProtect()


@app.errorhandler(404)
def page_not_found (e):
    return render_template("404.html") , 404 

@app.before_request
def before_request():
    g.nombre="Mario"
    print("before 1")

@app.after_request
def after_request(response):
    print("after 1")
    return response 

class ZodiacoForm(FlaskForm):
    nombre = StringField("Nombre", validators=[DataRequired()])
    apellido = StringField("Apellido", validators=[DataRequired()])
    anio = IntegerField("Año de nacimiento", validators=[DataRequired(), NumberRange(1900, 2025)])
    submit = SubmitField("Calcular Signo")

def calcular_signo_chino(anio):
    signos = [
        "Rata", "Buey", "Tigre", "Conejo", "Dragón", "Serpiente",
        "Caballo", "Cabra", "Mono", "Gallo", "Perro", "Cerdo"
    ]
    imagenes = [
        "rata.png", "buey.png", "tigre.png", "conejo.png", "dragon.png",
        "serpiente.png", "caballo.png", "cabra.png", "mono.png", 
        "gallo.png", "perro.png", "cerdo.png"
    ]
    indice = anio % 12
    return signos[indice], imagenes[indice]


#Clase CinepolisPython
class CinepolisPython:
    def __init__(self, nombre, cantidad_boletos, usa_tarjeta):
        self.nombre = nombre
        self.cantidad_boletos = cantidad_boletos
        self.usa_tarjeta = usa_tarjeta
        self.precio_boleto = 12
        self.total = 0

    def calcular_total(self):
        if self.cantidad_boletos > 7:
            return "Ups, no puedes comprar más de 7 boletos. Por favor, inténtalo de nuevo."

        if self.cantidad_boletos > 5:
            descuento = 0.15
        elif 3 <= self.cantidad_boletos <= 5:
            descuento = 0.10
        else:
            descuento = 0

        self.total = self.cantidad_boletos * self.precio_boleto
        self.total -= self.total * descuento

        if self.usa_tarjeta:
            self.total -= self.total * 0.10

        return round(self.total, 2)  # Redondeamos a dos decimales

    def generar_tiket(self):
        with open("TiketBoletosCinePython.txt", "a") as archivo:
            archivo.write("----- TIKET CINEPOLIS PYTHON GRACIAS POR TU COMPRA :) -----\n")
            archivo.write(f"Nombre del comprador: {self.nombre}\n")
            archivo.write(f"Cantidad de boletos solicitados: {self.cantidad_boletos}\n")
            archivo.write(f"Total a pagar: ${self.total:.2f}\n")
            archivo.write("-----------------------------------------------------------\n\n")
        return "Tiket generado con éxito. Por favor, revisa tu tiket."

# Configuración de la aplicación Flask
app = Flask(__name__)
compradores = []

@app.route("/Cinepolis", methods=["GET", "POST"])
def cinepolis():
    if request.method == "POST":
        nombre = request.form["nombre"]
        cantidad_boletos = int(request.form["cantidad_boletos"])
        usa_tarjeta = "tarjeta" in request.form

        cinepolis = CinepolisPython(nombre, cantidad_boletos, usa_tarjeta)
        total = cinepolis.calcular_total()

        if isinstance(total, str):
            return render_template("CinepolisPhyton.html", error=total, compradores=compradores)

        cinepolis.total = total
        cinepolis.generar_tiket()
        compradores.append({
            "nombre": nombre, 
            "cantidad_boletos": cantidad_boletos, 
            "usa_tarjeta": usa_tarjeta, 
            "total": total
        })

        return redirect(url_for("cinepolis"))

    return render_template("CinepolisPhyton.html", compradores=compradores)


@app.route("/salir")
def salir():
    return "¡Gracias por usar CinepolisPython! Hasta luego."

# Rutas adicionales (ejemplos)
@app.route("/")
def index():
    titulo = "IDGS801"
    lista = ["Pedro", "Juan", "Mario"]
    return render_template("index.html", titulo=titulo, lista=lista)

@app.route("/ejemplo1")
def ejemplo1():
    return render_template("ejemplo1.html")

@app.route("/ejemplo2")
def ejemplo2():
    return render_template("ejemplo2.html")

@app.route("/Hola")
def hola():
    return "Hola Mundo!!"

@app.route("/user/<string:user>")
def user(user):
    return f"Hola, {user}!"

@app.route("/numero/<int:n>")
def numero(n):
    return f"El número es: {n}"

@app.route("/user/<int:id>/<string:username>")
def username(id, username):
    return f"El usuario es: {username} con id: {id}"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return f"La suma es: {n1 + n2}"

@app.route("/default/")
@app.route("/default/<string:tem>")
def func1(tem='Juan'):
    return f"Hola, {tem}!"

@app.route("/form1/")
def form1():
    return '''
        <form>
            <label for="nombre">Nombre:</label>
            <input type="text" id="nombre" name="nombre">
        </form>
    '''

@app.route("/OperasBas", methods=["GET", "POST"])
def operas():
    resultado = None
    if request.method == "POST":
        num1 = float(request.form.get("n1"))
        num2 = float(request.form.get("n2"))
        operacion = request.form.get("operacion")

        if operacion == "sumar":
            resultado = num1 + num2
        elif operacion == "restar":
            resultado = num1 - num2
        elif operacion == "multiplicar":
            resultado = num1 * num2
        elif operacion == "dividir":
            if num2 == 0:
                resultado = "Error: División por cero"
            else:
                resultado = num1 / num2

    return render_template("OperasBas.html", resultado=resultado)


@app.route("/alumnos", methods = ["GET", "POST"])
def alumnos():
    print("alumno {}".format(g.nombre))
    mat=''
    nom=''
    ape=''
    email=''
    alumno_clase=forms.UserForm(request.form)
    if request.method=="POST" and alumno_clase.validate():
        mat = alumno_clase.matricula.data
        nom = alumno_clase.nombre.data
        ape = alumno_clase.apellido.data
        email = alumno_clase.email.data
        mensaje="Bienvenido {}".format(nom)
        flash(mensaje)
    return render_template("Alumnos.html", form=alumno_clase, mat=mat, nom=nom, ape=ape, email=email)

@app.route("/zodiaco", methods=["GET", "POST"])
def zodiaco():
    form = ZodiacoForm()
    resultado = None

    if form.validate_on_submit():
        nombre = form.nombre.data
        apellido = form.apellido.data
        anio = form.anio.data

        edad = datetime.now().year - anio
        signo, imagen = calcular_signo_chino(anio)

        resultado = {
            "nombre": nombre,
            "apellido": apellido,
            "edad": edad,
            "signo": signo,
            "imagen": imagen
        }

    return render_template("zodiacoChino.html", form=form, resultado=resultado)
   
    
# Ejecutar la aplicación
if __name__ == "__main__":
    csrf.init_app(app)
    app.run(debug=True, port=3000)



