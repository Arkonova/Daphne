# daphne/data_processing.py
from sklearn.preprocessing import StandardScaler
import numpy as np


def standardize_data(dataset, column_name):
    data = np.array([x[column_name] for x in dataset]).reshape(-1, 1)
    scaler = StandardScaler()
    standardized = scaler.fit_transform(data)
    return dataset.map(lambda x, std=standardized, idx=iter(range(len(standardized))):
                       {**x, column_name: std[next(idx)][0]})