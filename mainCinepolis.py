from flask import Flask, render_template, request

class CinepolisPython:
    def __init__(self, nombre, cantidad_boletos, usa_tarjeta):
        self.nombre = nombre
        self.cantidad_boletos = cantidad_boletos
        self.usa_tarjeta = usa_tarjeta
        self.precio_boleto = 12
        self.total = 0

    def calcular_total(self):
        if self.cantidad_boletos > 7:
            return "Ups no puedes comprar más de 7 boletos. Por favor, inténtalo de nuevo."

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

        return self.total

    def generar_tiket(self):
        with open("TiketBoletosCinePython.txt", "a") as archivo:
            archivo.write("----- TIKET CINEPOLIS PYTHON GRACIAS POR TU COMPRA :) -----\n")
            archivo.write(f"Nombre del comprador: {self.nombre}\n")
            archivo.write(f"Cantidad de boletos solicitados: {self.cantidad_boletos}\n")
            archivo.write(f"Total a pagar: ${self.total:.2f}\n")
            archivo.write("-----------------------------------------------------------\n\n")
        return "Tiket generado con éxito. Por favor, revisa tu tiket."

def realizar_compra(nombre, cantidad_boletos, usa_tarjeta):
    cinepolis = CinepolisPython(nombre, cantidad_boletos, usa_tarjeta)
    total = cinepolis.calcular_total()

    if isinstance(total, str):
        return total, None
    else:
        return None, total

# Configuración de Flask
app = Flask(__name__)

# Ruta principal
@app.route("/", methods=["GET", "POST"])  
def index():
    error = None
    total = None

    if request.method == "POST":
        nombre = request.form["nombre"]
        cantidad_boletos = int(request.form["cantidad_boletos"])
        usa_tarjeta = "tarjeta" in request.form

        error, total = realizar_compra(nombre, cantidad_boletos, usa_tarjeta)

        if not error and total is not None:
            cinepolis = CinepolisPython(nombre, cantidad_boletos, usa_tarjeta)
            cinepolis.total = total
            cinepolis.generar_tiket()

    return render_template("CinepolisPhyton.html", error=error, total=total) 

if __name__ == "__main__":
    app.run(debug=True, port=3000)