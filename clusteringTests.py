import unittest
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from CurvaCodo import realizar_clustering

class TestClustering(unittest.TestCase):

    def setUp(self):
        # configurando data de prueba
        data = {
            'MONTO_PIA': [100, 200, 300, 400, 500],
            'MONTO_PIM': [10, 20, 30, 40, 50],
            'MONTO_CERTIFICADO': [1000, 2000, 3000, 4000, 5000],
            'MONTO_COMPROMETIDO_ANUAL': [5, 15, 25, 35, 45],
            'MONTO_COMPROMETIDO': [2, 12, 22, 32, 42],
            'MONTO_DEVENGADO': [7, 17, 27, 37, 47],
            'MONTO_GIRADO': [9, 19, 29, 39, 49]
        }
        self.df = pd.DataFrame(data)
        scaler = StandardScaler()
        self.df_scaled = pd.DataFrame(scaler.fit_transform(self.df), columns=self.df.columns)

    def test_cluster_count(self):
        # probar si se crearon el correcto numero de clusters
        num_clusters = 3
        df_clustered, kmeans_model = realizar_clustering(self.df_scaled, num_clusters)
        self.assertEqual(len(np.unique(df_clustered['cluster'])), num_clusters)

    def test_dataframe_structure(self):
        # probar si el output del dataframe tiene la estructura esperada
        num_clusters = 3
        df_clustered, _ = realizar_clustering(self.df_scaled, num_clusters)
        self.assertIn('cluster', df_clustered.columns)
        self.assertEqual(len(df_clustered.columns), len(self.df_scaled.columns) + 1)

    def test_cluster_assignment(self):
        # probar si la asignacion del clsuter es consistente
        num_clusters = 3
        df_clustered, _ = realizar_clustering(self.df_scaled, num_clusters)
        clusters = df_clustered['cluster'].values
        self.assertTrue(all(isinstance(cluster, np.integer) for cluster in clusters))

    # casos extremos
    def test_edge_cases(self):
        # prueba de casos extremos como datos diminutos
        small_data = self.df_scaled.iloc[:2, :]
        df_clustered, _ = realizar_clustering(small_data, 2)
        self.assertEqual(len(np.unique(df_clustered['cluster'])), 2)

        # prueba de cero datos
        zero_data = pd.DataFrame(np.zeros((5, 7)), columns=self.df.columns)
        df_clustered, _ = realizar_clustering(zero_data, 2)
        self.assertEqual(len(np.unique(df_clustered['cluster'])), 1)

if __name__ == '__main__':
    unittest.main()
