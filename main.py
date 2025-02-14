

from flask import Flask, render_template, request, redirect, url_for

import forms



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


@app.route("/alumnos", methods=["GET","POST"]) 
def alumnos():
    mat=""
    nom=""
    ape=""
    email=""
    alumno_calse=forms.UserForm(request.form)
    if request.method=="POST":
        mat=alumno_calse.matricula.data
        ape=alumno_calse.apellido.data
        nom=alumno_calse.nombre.data
        email=alumno_calse.email.data
        print('Nombre: {}'.format(nom)) 
        return render_template("Alumnos.html" , form=alumno_calse)    
    
# Ejecutar la aplicación
if __name__ == "__main__":
    app.run(debug=True, port=3000)
