#Cargado de datos
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
import CurvaCodo as cc

archivo = "C:/Users/aldha/Documents/Datos_SI_Normalizado.xlsx" #Realizar el cambio según su PC

# Leer solo algunas columnas de un archivo Excel
columnas_a_leer = ['MONTO_PIA', 'MONTO_PIM', 'MONTO_CERTIFICADO', 'MONTO_COMPROMETIDO_ANUAL', 'MONTO_COMPROMETIDO', 'MONTO_DEVENGADO', 'MONTO_GIRADO']
df = pd.read_excel(archivo, usecols=columnas_a_leer)


#Eliminamos las columnas con valores Nan en el .csv
df = df.dropna()

# Realizar la normalización de los datos
scaler = StandardScaler()
df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

# Mostrar la curva del codo para seleccionar el número óptimo de clusters
cc.curva(archivo, columnas_a_leer, df)

# Realizar el clustering con un número determinado de clusters
num_clusters = 3  # Ajustar según el resultado de la curva del codo
df_clustered, kmeans_model = cc.realizar_clustering(df_scaled, num_clusters)

# Visualizar los clusters
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_clustered, x='MONTO_PIA', y='MONTO_PIM', hue='cluster', palette='viridis')
plt.title(f'Clustering de datos con KMeans (k={num_clusters})')
plt.xlabel('MONTO_PIA')
plt.ylabel('MONTO_PIM')
plt.legend(title='Cluster')
plt.show()