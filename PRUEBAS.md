
from pathlib import Path

import pandas as pd


BASE = Path(__file__).resolve().parent
ARCHIVO = BASE / "datos" / "estaciones.csv"
RESULTADOS = BASE / "resultados"

columnas = [
    "estacion",
    "pasajeros_manana",
    "pasajeros_tarde",
    "rutas_conectadas"
]

variables = [
    "pasajeros_manana",
    "pasajeros_tarde",
    "rutas_conectadas"
]


def ejecutar_pruebas():
    print("INICIO DE LAS PRUEBAS\n")

    # Prueba 1: comprobar que existe el CSV
    assert ARCHIVO.exists(), "No existe el archivo CSV."
    print("Prueba 1 aprobada: el CSV existe.")

    datos = pd.read_csv(ARCHIVO)

    # Prueba 2: comprobar las columnas
    assert all(c in datos.columns for c in columnas)
    print("Prueba 2 aprobada: las columnas son correctas.")

    # Prueba 3: comprobar la cantidad de estaciones
    assert len(datos) >= 3
    print("Prueba 3 aprobada: hay suficientes estaciones.")

    # Prueba 4: comprobar que no existan datos vacios
    assert not datos[columnas].isnull().any().any()
    print("Prueba 4 aprobada: no hay datos vacios.")

    # Prueba 5: comprobar los valores numericos
    for columna in variables:
        datos[columna] = pd.to_numeric(
            datos[columna], errors="raise"
        )

    assert (datos[variables] >= 0).all().all()
    print("Prueba 5 aprobada: los valores numericos son validos.")

    # Prueba 6: comprobar los archivos de salida
    csv_salida = RESULTADOS / "estaciones_agrupadas.csv"
    grafica = RESULTADOS / "grafica_clusters.png"

    if csv_salida.exists() and grafica.exists():
        print("Prueba 6 aprobada: existen los archivos de salida.")
    else:
        print(
            "Prueba 6 pendiente: ejecuta primero "
            "'python main.py' y vuelve a probar."
        )

    print("\nPruebas finalizadas.")


if __name__ == "__main__":
    ejecutar_pruebas()

# Pruebas del proyecto MetroCluster IA

## Objetivo

Comprobar que el programa lea los datos, valide el CSV y genere
los resultados del modelo K-Means.

## Pruebas realizadas

### Prueba 1. Existencia del archivo
Se comprueba que exista datos/estaciones.csv.

Resultado esperado: el archivo existe.

### Prueba 2. Columnas
Se comprueba que esten las cuatro columnas obligatorias.

Resultado esperado: las columnas son correctas.

### Prueba 3. Cantidad de estaciones
Se comprueba que existan al menos tres estaciones.

Resultado esperado: hay suficientes estaciones.

### Prueba 4. Datos vacios
Se comprueba que no existan celdas vacias.

Resultado esperado: no hay datos vacios.

### Prueba 5. Valores numericos
Se comprueba que las variables numericas tengan valores validos
y que no existan cantidades negativas.

Resultado esperado: los valores son validos.

### Prueba 6. Archivos generados
Se comprueba la existencia de los archivos de resultados.

Resultado esperado:
- resultados/estaciones_agrupadas.csv
- resultados/grafica_clusters.png

## Evidencias

Agregar capturas de pantalla de la ejecucion de main.py y pruebas.py.

## Conclusion

Las pruebas permiten comprobar la estructura del conjunto de datos
y verificar que el programa genere sus archivos de salida.
Los resultados definitivos se registraran despues de ejecutar el proyecto.
