# ![Daphne Logo](./daphne_logo.png) Daphne

![pypi package](https://img.shields.io/badge/pypi_package-v0.1.0b1-blue)
![build](https://img.shields.io/badge/build-passing-brightgreen)
![docs](https://img.shields.io/badge/docs-available-lightgrey)
![license](https://img.shields.io/badge/license-Apache%202.0-green)

## Overview

Daphne is a Python library designed to streamline data processing and preparation tasks. It includes tools for loading, cleaning, normalizing, and splitting datasets, as well as evaluating and managing them. Daphne is intended for data scientists and engineers who need a consistent and efficient way to handle datasets in their projects.

## Features

- **Data Loading**: Load data from various formats (CSV, JSON, Parquet, Excel).
- **Data Processing**: Clean, normalize, impute, and encode data with ease.
- **Dataset Preparation**: Split and balance datasets for training, validation, and testing.
- **Dataset Evaluation**: Analyze and visualize data distributions, correlations, and mutual information.
- **Parallel Processing**: Accelerate data processing tasks by leveraging multiple CPU cores.
- **Resource Management**: Monitor and manage memory usage to avoid resource bottlenecks.

## Installation

### Installation via PyPI (Coming Soon)
*Note: The installation via PyPI is currently under development and will be available soon.*
```bash
pip install daphne
```

### Installation from the latest [release](https://github.com/Arkonova/daphne/releases)

- **1** . Download the latest version of the .whl file from the releases page.
- **2** . Install the package using pip:
  - ```bash
    pip install Daphne-x.y.z.whl
    ```
    - Replace x.y.z with the appropriate release version.


## Usage
Here's a basic example of how to use Daphne in a data processing workflow:

```python
from Daphne import DataLoader, DataProcessor, DatasetPreparator, DatasetEvaluator

# Load the data
df = DataLoader.load_data('data.csv')

# Clean and process the data
processor = DataProcessor()
df = processor.clean_data(df)
df = processor.impute_missing_data(df)
df = processor.normalize_data(df)
df = processor.encode_categorical_data(df, ['category'])

# Split and evaluate the data
preparator = DatasetPreparator()
X_train, X_val, X_test, y_train, y_val, y_test = preparator.split_data(df, 'target')
evaluator = DatasetEvaluator()
evaluator.plot_distribution(df, 'target')
```
## Documentation
Full documentation for Daphne is available in the docs directory of this repository. It includes detailed guides on installation, usage, and the API reference.

## License
Daphne is licensed under the Apache 2.0 License. You are free to use, modify, and distribute this software under the terms of this license.