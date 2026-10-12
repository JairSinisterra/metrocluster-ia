
# Descripcion de los datos

## 1. Nombre del proyecto

MetroCluster IA: agrupamiento de estaciones del transporte masivo.

## 2. Objetivo

Aplicar aprendizaje no supervisado para encontrar grupos de estaciones
con comportamientos similares de demanda.

## 3. Fuente de los datos

Se creo un archivo CSV con informacion simulada de 15 estaciones.
Los datos son academicos y no corresponden a cifras oficiales.

## 4. Variables

- estacion: nombre de la estacion.
- pasajeros_manana: pasajeros simulados durante la manana.
- pasajeros_tarde: pasajeros simulados durante la tarde.
- rutas_conectadas: numero simulado de rutas o conexiones.

## 5. Preparacion

Se utiliza pandas para leer los datos.
Se comprueba que las columnas existan y que no haya valores vacios
ni cantidades negativas.
Despues, StandardScaler estandariza las variables numericas.

## 6. Algoritmo

Se utiliza K-Means con tres grupos.
El algoritmo busca estaciones similares segun las variables numericas.
No necesita etiquetas de grupos previamente definidas.

## 7. Resultados

El programa guarda un CSV con el grupo asignado a cada estacion
y una grafica que permite visualizar los resultados.

Los grupos se identifican como demanda baja, media y alta
segun la demanda promedio de sus estaciones.

## 8. Limitaciones

La muestra es pequena y simulada.
Por eso, los resultados no describen necesariamente el comportamiento
real del Metro de Medellin.
