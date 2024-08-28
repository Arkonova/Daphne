# src/resource_management.py

import os
import pandas as pd
import psutil
from tempfile import mkdtemp

class ResourceManager:
    """
    A class for managing system resources, such as memory usage. This class provides methods
    to monitor memory usage and to offload data to temporary files when memory usage is high.
    """

    def __init__(self, max_memory_usage: float = 0.75):
        self.max_memory_usage = max_memory_usage
        self.temp_dir = mkdtemp()
    def check_memory(self):
        """
        Checks the current memory usage and frees up resources if the usage exceeds the threshold.

        Raises:
            ValueError: If memory check or resource management fails.
        """
        try:
            used_memory = psutil.virtual_memory().percent
            if used_memory > self.max_memory_usage * 100:
                self.free_up_memory()
        except Exception as e:
            raise ValueError(f"Failed to check memory usage: {e}")

    def free_up_memory(self, df: pd.DataFrame):
        """
        Frees up memory by caching data to disk when memory usage is high.

        Args:
            df (pd.DataFrame): The DataFrame to cache and clear from memory.
        """
        try:
            cache_file = os.path.join(self.temp_dir, 'data_cache.pkl')
            df.to_pickle(cache_file)
            df.drop(df.index, inplace=True)
        except Exception as e:
            raise ValueError(f"Failed to free up memory: {e}")
