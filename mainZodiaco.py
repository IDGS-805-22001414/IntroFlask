from datetime import datetime
from flask import Flask, render_template, request, url_for
from forms import ZodiacoForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mi_clave_secreta'


def calcular_signo_chino(anio):
    signos = [
        "Mono", "Gallo", "Perro", "Cerdo", "Rata", "Buey", "Tigre", "Conejo", "Dragon", "Serpiente", "Caballo", "Cabra"
    ]
    
    imagenes = [
        "monoZodiacoChino.jpg" , "gallo.jpg" , "perro.jpeg" , "cerdo.jpg" , "rataZodiacoChino.jpg", "bueyZodiacoChino.png", "tigreZodiacoChino.jpeg",
        "conejoZodiacoChino.jpg", "dragonZodiacoChino.png", "serpienteZodiacoChino.png",
        "caballoZodiacoChino.png", "cabra.jpg"
       
    ]

    indice = anio % 12
    return signos[indice], imagenes[indice]


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
            "imagen": url_for('static', filename=f'bootstrap/bootstrap/img/{imagen}')
        }

    return render_template("zodiacoChino.html", form=form, resultado=resultado)


if __name__ == "__main__":
    app.run(debug=True, port=3000)
