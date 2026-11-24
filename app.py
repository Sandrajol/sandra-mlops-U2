from flask import Flask, render_template, request

from historial import guardar_prediccion, obtener_reporte
from modelo import clasificar_estado

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def inicio():
    resultado = None
    error = None

    if request.method == "POST":
        try:
            cantidad = int(request.form.get("cantidad_sintomas", ""))
            dias = int(request.form.get("dias_sintomas", ""))
            intensidad = int(request.form.get("intensidad", ""))
        except ValueError:
            error = "Completa los tres campos con números enteros."
        else:
            try:
                resultado = clasificar_estado(cantidad, dias, intensidad)
            except ValueError as exc:
                error = str(exc)
            else:
                guardar_prediccion(cantidad, dias, intensidad, resultado)

    return render_template("index.html", resultado=resultado, error=error)


@app.route("/reporte")
def reporte():
    return render_template("reporte.html", reporte=obtener_reporte())


@app.route("/api/reporte")
def reporte_json():
    return obtener_reporte()


if __name__ == "__main__":
    app.run()