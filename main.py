
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score


# 1. Ubicacion de los archivos
BASE = Path(__file__).resolve().parent
ARCHIVO = BASE / "datos" / "estaciones.csv"
SALIDA = BASE / "resultados"

SALIDA.mkdir(exist_ok=True)


# 2. Cargar los datos
datos = pd.read_csv(ARCHIVO)

columnas = [
    "estacion",
    "pasajeros_manana",
    "pasajeros_tarde",
    "rutas_conectadas"
]

if not all(columna in datos.columns for columna in columnas):
    raise ValueError("Faltan columnas obligatorias en el CSV.")

if datos.empty:
    raise ValueError("El archivo CSV no contiene datos.")

if datos[columnas].isnull().any().any():
    raise ValueError("Hay datos vacios en el archivo CSV.")

variables = [
    "pasajeros_manana",
    "pasajeros_tarde",
    "rutas_conectadas"
]

for columna in variables:
    datos[columna] = pd.to_numeric(
        datos[columna], errors="raise"
    )

if (datos[variables] < 0).any().any():
    raise ValueError("Los valores numericos no pueden ser negativos.")

if len(datos) < 3:
    raise ValueError("Se necesitan al menos 3 estaciones.")

print("Datos cargados correctamente.")
print("Total de estaciones:", len(datos))


# 3. Preparar los datos
X = datos[variables]

escalador = StandardScaler()
X_escalado = escalador.fit_transform(X)


# 4. Crear y entrenar el modelo K-Means
modelo = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

datos["grupo"] = modelo.fit_predict(X_escalado)


# 5. Calcular la demanda promedio
datos["demanda_promedio"] = (
    datos["pasajeros_manana"]
    + datos["pasajeros_tarde"]
) / 2


# 6. Poner nombre a los grupos segun su demanda
promedios = datos.groupby("grupo")[
    "demanda_promedio"
].mean()

orden = promedios.sort_values().index.tolist()

nombres = {
    orden[0]: "Demanda baja",
    orden[1]: "Demanda media",
    orden[2]: "Demanda alta"
}

datos["categoria"] = datos["grupo"].map(nombres)


# 7. Mostrar los resultados
print("\nRESULTADOS DEL MODELO")

print(
    datos[
        ["estacion", "grupo", "demanda_promedio", "categoria"]
    ].to_string(index=False)
)


# 8. Evaluar el agrupamiento
puntaje = silhouette_score(X_escalado, datos["grupo"])

print("\nPuntaje Silhouette:", round(puntaje, 3))


# 9. Guardar los resultados en CSV
archivo_resultados = SALIDA / "estaciones_agrupadas.csv"

datos.to_csv(archivo_resultados, index=False)

print("\nArchivo CSV guardado correctamente.")


# 10. Crear la grafica
colores = {
    "Demanda baja": "green",
    "Demanda media": "orange",
    "Demanda alta": "red"
}

plt.figure(figsize=(9, 5))

for categoria in nombres.values():
    grupo = datos[datos["categoria"] == categoria]

    plt.scatter(
        grupo["pasajeros_manana"],
        grupo["pasajeros_tarde"],
        label=categoria,
        color=colores[categoria],
        s=80
    )

plt.xlabel("Pasajeros en la manana")
plt.ylabel("Pasajeros en la tarde")
plt.title("Agrupamiento de estaciones con K-Means")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig(SALIDA / "grafica_clusters.png")
plt.close()

print("Grafica guardada correctamente.")
print("\nProyecto terminado.")
 