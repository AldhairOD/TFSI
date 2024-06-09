#Cargado de datos
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

archivo = "C:/Users/aldha/Documents/Datos_SI_Normalizado.xlsx" #Realizar el cambio según su PC

# Leer solo algunas columnas de un archivo Excel
columnas_a_leer = ['MONTO_PIA', 'MONTO_PIM', 'MONTO_CERTIFICADO', 'MONTO_COMPROMETIDO_ANUAL', 'MONTO_COMPROMETIDO', 'MONTO_DEVENGADO', 'MONTO_GIRADO']
df = pd.read_excel(archivo, usecols=columnas_a_leer)

#Mostramos algunos datos
df.head(14000)
#Mostramos los últimos datos
df.tail()
#Revisamos la información del archivo .csv
df.info()

#Eliminamos las columnas con valores Nan en el .csv
data_clean = df.dropna()

#Estandarizamos los datos para poder utilizarlos en el algoritmo K-Means
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data_clean[columnas_a_leer])

#Determinamos el número óptimo de clusters usando el método del codo
sse = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(data_scaled)
    sse.append(kmeans.inertia_)
