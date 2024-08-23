import os
import pandas as pd


def save_dataset(dataset, path='processed_data.csv', format='csv'):
    current_dir = os.getcwd()  # Получаем текущую директорию
    save_path = os.path.join(current_dir, path)

    if format == 'csv':
        df = pd.DataFrame(dataset)
        df.to_csv(save_path, index=False)
    elif format == 'json':
        df = pd.DataFrame(dataset)
        df.to_json(save_path)
    elif format == 'parquet':
        df = pd.DataFrame(dataset)
        df.to_parquet(save_path)
    else:
        raise ValueError(f"Unsupported format: {format}")