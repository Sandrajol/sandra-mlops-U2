# Entrega 2 de MLOps

## Problema

Se desarrolla una aplicación que permite introducir información sobre
los síntomas de un paciente y obtener una clasificación simulada.
La solución inicial utiliza Python y Flask y se ejecuta mediante Docker.

## Propósito

Este repositorio permite mantener el control de versiones de la aplicación,
incorporar nuevos requerimientos mediante ramas y pull requests, y automatizar
las pruebas y la publicación de la imagen Docker mediante GitHub Actions.

Los nuevos requerimientos incluyen la categoría ENFERMEDAD TERMINAL y un
reporte con el número de predicciones por categoría, las últimas cinco
predicciones y la fecha de la última predicción.

## Estructura prevista

| Archivo o carpeta | Función |
|---|---|
| README.md | Descripción del proyecto e instrucciones de ejecución. |
| app.py | Servicio web y procesamiento de las solicitudes. |
| modelo.py | Función de clasificación simulada. |
| templates/ | Páginas del formulario y del reporte. |
| requirements.txt | Dependencias de Python. |
| Dockerfile | Construcción y ejecución de la imagen. |
| tests/ | Pruebas automatizadas. |
| .github/workflows/ | Configuración de GitHub Actions. |

La estructura se incorporará progresivamente siguiendo las ramas,
los commits y los pull requests solicitados en la actividad.

## Alcance académico

Las clasificaciones se generan mediante reglas programadas para el ejercicio.
Los datos usados en las pruebas son ficticios.

## Autora

Sandra Jimena Orozco Lagos
