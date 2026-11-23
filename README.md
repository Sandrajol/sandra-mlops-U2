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

## Estado de la solución inicial

La aplicación inicial recibe tres valores enteros:

- Cantidad de síntomas, mayor o igual a cero.
- Días con síntomas, mayor o igual a cero.
- Intensidad de los síntomas, entre cero y diez.

La función simulada devuelve uno de estos cuatro estados:

- NO ENFERMO.
- ENFERMEDAD LEVE.
- ENFERMEDAD AGUDA.
- ENFERMEDAD CRÓNICA.

La quinta categoría y el reporte se incorporarán en los siguientes pasos
de la actividad.

## Estructura de la solución inicial

| Archivo o carpeta | Función |
|---|---|
| README.md | Descripción del proyecto e instrucciones de ejecución. |
| app.py | Servicio web y procesamiento de las solicitudes. |
| modelo.py | Función de clasificación simulada. |
| templates/index.html | Formulario para introducir los datos. |
| requirements.txt | Dependencias de Python. |
| Dockerfile | Construcción y ejecución de la imagen. |

Durante el desarrollo se agregarán el reporte de estadísticas, las pruebas
automatizadas en tests/ y los workflows en .github/workflows/.

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
docker build -t clasificador-mlops:1.0 .
```

El punto final indica que Docker debe utilizar la carpeta actual.

## Ejecutar el contenedor

```powershell
docker run --rm -p 127.0.0.1:5001:5000 clasificador-mlops:1.0
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

Estos cuatro casos se comprobaron durante la entrega 1, tanto en la
ejecución local como dentro del contenedor Docker.

## Alcance académico

Las clasificaciones se generan mediante reglas programadas para el
ejercicio. Los datos utilizados en las pruebas son ficticios.

## Autora

Sandra Jimena Orozco Lagos