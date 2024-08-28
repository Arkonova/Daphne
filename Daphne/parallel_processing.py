# src/parallel_processing.py

import pandas as pd
import numpy as np
from multiprocessing import Pool

class ParallelProcessor:
    """
    A class for parallel processing of data using multiple CPU cores. This class enables the
    application of a function to DataFrame partitions in parallel.
    """

    def apply_parallel(self, df: pd.DataFrame, func, num_partitions: int = 4) -> pd.DataFrame:
        """
        Applies a function to a DataFrame in parallel, splitting the data into partitions.

        Args:
            df (pd.DataFrame): The input DataFrame.
            func (callable): The function to apply to each partition.
            num_partitions (int): The number of partitions to split the DataFrame into.

        Returns:
            pd.DataFrame: The DataFrame with the function applied to all partitions.

        Raises:
            ValueError: If parallel processing fails.
        """
        try:
            df_split = np.array_split(df, num_partitions)
            with Pool(num_partitions) as pool:
                df_processed = pd.concat(pool.map(func, df_split))
            return df_processed
        except Exception as e:
            raise ValueError(f"Failed to process data in parallel: {e}")
