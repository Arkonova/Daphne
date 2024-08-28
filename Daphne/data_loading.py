import pandas as pd
import os

class DataLoader:
    """
    A class to load data from various file formats. The class can automatically determine the
    file format based on the file extension and load the data accordingly.
    """

    @staticmethod
    def load_data(file_path: str) -> pd.DataFrame:
        """
        Loads data from a file, automatically detecting the format based on the file extension.

        Args:
            file_path (str): The path to the data file.

        Returns:
            pd.DataFrame: A DataFrame containing the loaded data.

        Raises:
            ValueError: If the file extension is not recognized or if loading fails.
        """
        _, file_extension = os.path.splitext(file_path)
        file_extension = file_extension.lower()

        try:
            if file_extension == '.csv':
                return pd.read_csv(file_path)
            elif file_extension == '.json':
                return pd.read_json(file_path)
            elif file_extension == '.parquet':
                return pd.read_parquet(file_path)
            elif file_extension in ['.xls', '.xlsx']:
                return pd.read_excel(file_path)
            else:
                raise ValueError(f"Unsupported file format: {file_extension}")
        except Exception as e:
            raise ValueError(f"Failed to load data from {file_path}: {e}")

