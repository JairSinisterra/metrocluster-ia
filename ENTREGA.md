
# MetroCluster IA

Proyecto academico de Inteligencia Artificial que utiliza aprendizaje
no supervisado para agrupar estaciones del transporte masivo.

## Objetivo

Encontrar grupos de estaciones con caracteristicas similares
usando datos simulados de pasajeros y conexiones.

## Tecnologias

- Python
- pandas
- scikit-learn
- matplotlib
- Visual Studio Code
- Git y GitHub

## Archivos principales

- datos/estaciones.csv: datos de entrada.
- main.py: programa de inteligencia artificial.
- pruebas.py: pruebas basicas del proyecto.
- DESCRIPCION_DATOS.md: descripcion de los datos.
- PRUEBAS.md: documentacion de las pruebas.
- ENTREGA.md: enlaces de entrega.
- requirements.txt: bibliotecas necesarias.
- resultados/: archivos generados por el programa.

## Instalacion

Crear y activar un entorno virtual:

python3 -m venv .venv

source .venv/bin/activate

Instalar las bibliotecas:

python -m pip install -r requirements.txt

## Ejecucion

Ejecutar el modelo:

python main.py

Ejecutar las pruebas:

python pruebas.py

## Algoritmo

Se utiliza K-Means con tres grupos.
Las variables se estandarizan con StandardScaler.

## Resultados

El programa genera un archivo CSV con las estaciones agrupadas
y una grafica PNG.

## Nota

Los datos son simulados y no representan estadisticas oficiales
del Metro de Medellin.
