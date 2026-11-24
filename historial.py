import csv
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from threading import Lock

ARCHIVO = Path(__file__).resolve().parent / "datos" / "predicciones.csv"

CATEGORIAS = (
    "NO ENFERMO",
    "ENFERMEDAD LEVE",
    "ENFERMEDAD AGUDA",
    "ENFERMEDAD CRÓNICA",
    "ENFERMEDAD TERMINAL",
)

CAMPOS = (
    "fecha",
    "cantidad_sintomas",
    "dias_sintomas",
    "intensidad",
    "resultado",
)

BLOQUEO = Lock()


def guardar_prediccion(cantidad_sintomas, dias_sintomas, intensidad, resultado):
    """Agrega una predicción al historial."""
    registro = {
        "fecha": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "cantidad_sintomas": cantidad_sintomas,
        "dias_sintomas": dias_sintomas,
        "intensidad": intensidad,
        "resultado": resultado,
    }

    with BLOQUEO:
        ARCHIVO.parent.mkdir(parents=True, exist_ok=True)
        necesita_encabezado = not ARCHIVO.exists() or ARCHIVO.stat().st_size == 0

        with ARCHIVO.open("a", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=CAMPOS)

            if necesita_encabezado:
                escritor.writeheader()

            escritor.writerow(registro)


def obtener_reporte():
    """Consulta el historial y calcula las estadísticas."""
    with BLOQUEO:
        if ARCHIVO.exists():
            with ARCHIVO.open(newline="", encoding="utf-8") as archivo:
                registros = list(csv.DictReader(archivo))
        else:
            registros = []

    conteos = Counter(registro["resultado"] for registro in registros)

    return {
        "totales_por_categoria": {
            categoria: conteos[categoria] for categoria in CATEGORIAS
        },
        "ultimas_cinco": list(reversed(registros[-5:])),
        "fecha_ultima": registros[-1]["fecha"] if registros else None,
    }