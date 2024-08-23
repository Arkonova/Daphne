import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

def fill_missing(df, method='mean'):
    if method == 'mean':
        return df.fillna(df.mean())
    elif method == 'median':
        return df.fillna(df.median())
    elif method == 'mode':
        return df.fillna(df.mode().iloc[0])
    else:
        return df.fillna(method)

def normalize(df):
    return (df - df.min()) / (df.max() - df.min())

def remove_duplicates(df):
    return df.drop_duplicates()

def scale_data(df):
    scaler = StandardScaler()
    return pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

def encode_categories(df):
    encoder = LabelEncoder()
    for column in df.select_dtypes(include=['object']).columns:
        df[column] = encoder.fit_transform(df[column])
    return df
