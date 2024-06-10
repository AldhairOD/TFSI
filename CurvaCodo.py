import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


def curva(archivo, columnas, df):
    # Elbow method para encontrar el número óptimo de clusters
    distortions = []
    K = range(1, 11)
    for k in K:
        kmeans = KMeans(n_clusters=k)
        kmeans.fit(df)
        distortions.append(kmeans.inertia_)

    # Graficar la curva del codo
    plt.figure(figsize=(8, 5))
    plt.plot(K, distortions, 'bx-')
    plt.xlabel('Número de clusters')
    plt.ylabel('Distorsión')
    plt.title('Método del Codo para encontrar el k óptimo')
    plt.show()
