import pandas as pd
import json
import pyarrow.parquet as pq
import requests

def load_csv(filepath, chunksize=None):
    return pd.read_csv(filepath, chunksize=chunksize)

def load_json(filepath):
    with open(filepath, 'r') as file:
        return pd.DataFrame(json.load(file))

def load_parquet(filepath):
    return pd.read_parquet(filepath)

def load_excel(filepath, sheet_name=0):
    return pd.read_excel(filepath, sheet_name=sheet_name)

def load_from_db(connection_string, query):
    import sqlalchemy
    engine = sqlalchemy.create_engine(connection_string)
    return pd.read_sql(query, engine)

def load_from_api(url, params=None):
    response = requests.get(url, params=params)
    data = response.json()
    return pd.DataFrame(data)
