# Entrega 2 de MLOps

## Problema

Se desarrolla una aplicación que permite introducir información sobre los
síntomas de un paciente y obtener una clasificación simulada. La solución
inicial utiliza Python y Flask y se ejecuta mediante Docker.

## Propósito

Este repositorio permite mantener el control de versiones de la aplicación,
incorporar nuevos requerimientos mediante ramas y pull requests, y automatizar
las pruebas y la publicación de la imagen Docker mediante GitHub Actions.

Los nuevos requerimientos incluyen la categoría ENFERMEDAD TERMINAL y un
reporte con el número de predicciones por categoría, las últimas cinco
predicciones y la fecha de la última predicción.

## Estado actual de la solución

La aplicación inicial recibe tres valores enteros:

- Cantidad de síntomas, mayor o igual a cero.
- Días con síntomas, mayor o igual a cero.
- Intensidad de los síntomas, entre cero y diez.

La función simulada devuelve uno de estos cinco estados:

- NO ENFERMO.
- ENFERMEDAD LEVE.
- ENFERMEDAD AGUDA.
- ENFERMEDAD CRÓNICA.
- ENFERMEDAD TERMINAL

La quinta categoría y el reporte de estadísticas ya estan implementados.

## Estructura de la solución inicial

| Archivo o carpeta | Función |
|---|---|
| README.md | Descripción del proyecto e instrucciones de ejecución. |
| app.py | Servicio web y procesamiento de las solicitudes. |
| modelo.py | Función de clasificación simulada. |
| templates/index.html | Formulario para introducir los datos. |
| requirements.txt | Dependencias de Python. |
| Dockerfile | Construcción y ejecución de la imagen. |

El reporte de estadísticas, las pruebas automatizadas en tests/
y el workflow en .github/workflows/ ya están implementados.

## Requisito para ejecutar la aplicación

Tener Docker instalado y en ejecución. En Windows, abrir Docker Desktop.

Comprobar su funcionamiento desde una terminal:

```powershell
docker version
```

Deben aparecer las secciones Client y Server.

## Construir la imagen Docker

Abrir una terminal en la carpeta que contiene el Dockerfile y ejecutar:

```powershell
docker build -t clasificador-mlops:2.0 .
```

El punto final indica que Docker debe utilizar la carpeta actual.

## Ejecutar el contenedor

```powershell
docker run --rm -p 127.0.0.1:5001:5000 --mount type=volume,source=mlops-u2-datos,target=/app/datos clasificador-mlops:2.0
```

Mantener la terminal abierta y acceder a:

http://127.0.0.1:5001

Docker conecta el puerto 5001 del computador con el puerto 5000
del contenedor.

Para detener el contenedor, presionar Ctrl + C en la terminal.

## Probar el formulario

Introducir los tres valores y pulsar Clasificar.

| Cantidad de síntomas | Días con síntomas | Intensidad | Resultado esperado |
|---:|---:|---:|---|
| 0 | 0 | 0 | NO ENFERMO |
| 2 | 3 | 4 | ENFERMEDAD LEVE |
| 2 | 3 | 8 | ENFERMEDAD AGUDA |
| 2 | 40 | 4 | ENFERMEDAD CRÓNICA |
| 3 | 100 | 9 | ENFERMEDAD TERMINAL |

Los cuatro casos originales se comprobaron en la entrega 1. La categoría terminal 
se incorporó y comprobó en la entrega 2.

## Alcance académico

Las clasificaciones se generan mediante reglas programadas para el
ejercicio. Los datos utilizados en las pruebas son ficticios.

## Reporte de predicciones

Cada predicción exitosa del formulario se registra en
datos/predicciones.csv.

El reporte muestra:

- Número total de predicciones por cada una de las cinco categorías.
- Últimas cinco predicciones, comenzando por la más reciente.
- Fecha y hora de la última predicción, expresadas en UTC.

Consultar el reporte en tablas:
http://127.0.0.1:5001/reporte

Consultar el reporte en formato JSON:
http://127.0.0.1:5001/api/reporte

El volumen Docker mlops-u2-datos conserva el historial al detener
y volver a iniciar el contenedor con el mismo comando.

Se comprobó que los registros, los totales y la fecha permanecen
después de reiniciar el contenedor.

## Pruebas automatizadas

Desde la carpeta del proyecto, instalar las dependencias y ejecutar:

```powershell
python -m pip install -r requirements.txt
python -m pip install pytest==9.2.0
python -m pytest tests -v
```

Las tres pruebas verifican las cinco categorías, el reporte vacío
y el registro de predicciones con sus estadísticas.

Las pruebas del historial utilizan archivos temporales independientes.

## Integración y entrega continuas

El workflow se encuentra en .github/workflows/ci-cd.yml.

En cada pull request dirigido a main:

1. Publica un comentario de inicio.
2. Ejecuta las pruebas automatizadas.
3. Publica un comentario de éxito si las pruebas pasan.

Después de incorporar cambios en main:

1. Vuelve a ejecutar las pruebas.
2. Construye la imagen Docker.
3. Publica la imagen en GitHub Container Registry.

La rama main requiere un pull request y pruebas exitosas antes del merge.

## Ejecutar la imagen publicada

Descargar la imagen:

```powershell
docker pull ghcr.io/sandrajol/sandra-mlops-u2:latest
```

Ejecutar con un volumen para conservar el historial:

```powershell
docker run --rm -p 127.0.0.1:5001:5000 --mount type=volume,source=mlops-u2-datos,target=/app/datos ghcr.io/sandrajol/sandra-mlops-u2:latest
```

Abrir el formulario en http://127.0.0.1:5001
y el reporte en http://127.0.0.1:5001/reporte.

La imagen también se publica con una etiqueta correspondiente
al identificador del commit.


## Sandra Jimena Orozco Lagos
