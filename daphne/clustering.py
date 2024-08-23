# daphne/clustering.py
from sklearn.cluster import KMeans
import numpy as np
def cluster_data(dataset, column_name='input_ids', n_clusters=3):
    kmeans = KMeans(n_clusters=n_clusters)
    data = np.array([x[column_name] for x in dataset]).reshape(-1, 1)
    clusters = kmeans.fit_predict(data)
    return dataset.map(lambda x, i=clusters: {'cluster': clusters[i]}, with_indices=True)
