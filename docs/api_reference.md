# API Reference

This document provides detailed information on the classes and methods available in the Daphne library.

---

## DataLoader

### Methods

- **`load_data(file_path: str) -> pd.DataFrame`**

    Loads data from a specified file path. Supports CSV, JSON, Parquet, and Excel formats.

    **Parameters**:
    - `file_path`: Path to the data file.

    **Returns**:
    - `pd.DataFrame`: Loaded data.

    **Raises**:
    - `ValueError`: If the file format is unsupported or loading fails.

---

## DataProcessor

### Methods

- **`clean_data(df: pd.DataFrame) -> pd.DataFrame`**

    Cleans the data by removing duplicates and missing values.

    **Parameters**:
    - `df`: DataFrame to be cleaned.

    **Returns**:
    - `pd.DataFrame`: Cleaned DataFrame.

    **Raises**:
    - `ValueError`: If the DataFrame is empty or cleaning fails.

- **`normalize_data(df: pd.DataFrame, method: str = 'standard') -> pd.DataFrame`**

    Normalizes numeric data using either Standard or Min-Max scaling.

    **Parameters**:
    - `df`: DataFrame to be normalized.
    - `method`: Normalization method ('standard' or 'minmax').

    **Returns**:
    - `pd.DataFrame`: Normalized DataFrame.

    **Raises**:
    - `ValueError`: If the method is invalid or normalization fails.

- **`impute_missing_data(df: pd.DataFrame, strategy: str = 'mean') -> pd.DataFrame`**

    Imputes missing data using specified strategy ('mean', 'median', 'most_frequent').

    **Parameters**:
    - `df`: DataFrame with missing data.
    - `strategy`: Imputation strategy.

    **Returns**:
    - `pd.DataFrame`: DataFrame with imputed values.

    **Raises**:
    - `ValueError`: If imputation fails.

- **`encode_categorical_data(df: pd.DataFrame, columns: list) -> pd.DataFrame`**

    Encodes categorical columns using `OneHotEncoder`.

    **Parameters**:
    - `df`: DataFrame with categorical columns.
    - `columns`: List of columns to encode.

    **Returns**:
    - `pd.DataFrame`: DataFrame with encoded columns.

    **Raises**:
    - `ValueError`: If encoding fails.

---

## DatasetPreparator

### Methods

- **`split_data(df: pd.DataFrame, target_column: str, test_size: float = 0.2, val_size: float = 0.1) -> tuple`**

    Splits data into training, validation, and test sets.

    **Parameters**:
    - `df`: DataFrame to be split.
    - `target_column`: Column to predict.
    - `test_size`: Proportion of data for testing.
    - `val_size`: Proportion of data for validation.

    **Returns**:
    - `tuple`: `(X_train, X_val, X_test, y_train, y_val, y_test)`

    **Raises**:
    - `ValueError`: If splitting fails.

- **`balance_classes(df: pd.DataFrame, target_column: str) -> pd.DataFrame`**

    Balances class distribution by oversampling the minority class.

    **Parameters**:
    - `df`: DataFrame with imbalanced classes.
    - `target_column`: Column with class labels.

    **Returns**:
    - `pd.DataFrame`: Balanced DataFrame.

    **Raises**:
    - `ValueError`: If balancing fails.

---

## DatasetEvaluator

### Methods

- **`plot_distribution(df: pd.DataFrame, column: str)`**

    Plots the distribution of a specified column.

    **Parameters**:
    - `df`: DataFrame containing the data.
    - `column`: Column to plot.

    **Raises**:
    - `ValueError`: If plotting fails.

- **`check_correlations(df: pd.DataFrame)`**

    Displays a correlation matrix for the DataFrame.

    **Parameters**:
    - `df`: DataFrame to check correlations.

    **Raises**:
    - `ValueError`: If checking correlations fails.

- **`calculate_mutual_information(df: pd.DataFrame, target_column: str) -> pd.Series`**

    Calculates mutual information between features and target column.

    **Parameters**:
    - `df`: DataFrame with features.
    - `target_column`: Target column for mutual information calculation.

    **Returns**:
    - `pd.Series`: Mutual information scores.

    **Raises**:
    - `ValueError`: If calculation fails.

---

## ParallelProcessor

### Methods

- **`apply_parallel(df: pd.DataFrame, func, num_partitions: int = 4) -> pd.DataFrame`**

    Applies a function to the DataFrame in parallel.

    **Parameters**:
    - `df`: DataFrame to process.
    - `func`: Function to apply.
    - `num_partitions`: Number of partitions to split the data.

    **Returns**:
    - `pd.DataFrame`: Processed DataFrame.

    **Raises**:
    - `ValueError`: If parallel processing fails.

---

## ResourceManager

### Methods

- **`check_memory()`**

    Checks current memory usage and frees resources if necessary.

    **Raises**:
    - `ValueError`: If memory check fails.

- **`free_up_memory(df: pd.DataFrame)`**

    Frees up memory by caching data to disk.

    **Parameters**:
    - `df`: DataFrame to cache.

    **Raises**:
    - `ValueError`: If memory freeing fails.

---
