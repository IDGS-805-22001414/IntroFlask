from flask import Flask, render_template, request

app = Flask(__name__)

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
    return f"El numero es: {n}"

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

@app.route("/OperasBas", methods=["GET", "POST"])  # Añadido methods=["GET", "POST"]
def operas():
    resultado = None
    if request.method == "POST":
        num1 = float(request.form.get("n1"))  # Convertir a float
        num2 = float(request.form.get("n2"))  # Convertir a float
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

    return render_template("OperasBas.html", resultado=resultado) # Pasar resultado a la plantilla


if __name__ == "__main__":  # Corregido a "__main__"
    app.run(debug=True, port=3000)