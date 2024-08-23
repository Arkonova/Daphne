
# ![Daphne Logo](./daphne_logo.png) Daphne

![pypi package](https://img.shields.io/badge/pypi_package-v0.1.0-blue)
![build](https://img.shields.io/badge/build-passing-brightgreen)
![docs](https://img.shields.io/badge/docs-unknown-lightgrey)
![license](https://img.shields.io/badge/license-Apache%202.0-green)

Daphne is a Python library designed for efficient data processing, catering to both small and large datasets. It offers functionalities for data standardization, clustering, stream processing, and integration with popular datasets libraries like Hugging Face's `datasets` and TensorFlow Datasets (TFDS).

## Features
- **Data Standardization:** Normalize and prepare data for various machine learning tasks.
- **Stream Processing:** Efficiently handle and process large datasets in a streaming mode, minimizing memory usage.
- **Task-Specific Preparation:** Customizable data preparation for classification, clustering, NLP, and image generation.
- **Seamless Integration:** Directly works with Hugging Face Datasets, TFDS, and other sources.
- **Resource Efficiency:** Optimized for minimal memory footprint even with large datasets.
- **Data Compression:** Save processed data in compressed formats for efficient storage.

## Installation

### Installation via PyPI (Coming Soon)
*Note: The installation via PyPI is currently under development and will be available soon.*
```bash
pip install daphne
```

## Installation from the latest [release](https://github.com/Arkonova/daphne/releases)

- **1** . Download the latest version of the .whl file from the releases page.
- **2** . Install the package using pip:
  - ```bash
    pip install daphne-x.y.z.whl
    ```
    - Replace x.y.z with the appropriate release version.



## Quick Start
```python
import daphne as dp

# Load and process dataset
dataset = dp.load_dataset('your_dataset_name')
processed_data = dp.prepare_data_for_task(dataset, task_type='classification')

# Save processed data
dp.save_data(processed_data, 'processed_data')

# Load saved data
loaded_data = dp.load_data('processed_data')

# Stream processing
dp.enable_stream_mode()
streamed_data = dp.process_streaming_dataset(dataset)
```

## Full Functionality

### Data Loading
```python
dataset = dp.load_dataset('dataset_name')
```
Loads a dataset, supporting multiple formats.

### Data Preparation
```python
processed_data = dp.prepare_data_for_task(dataset, task_type='classification')
```
Prepares data for specific machine learning tasks.

### Data Saving
```python
dp.save_data(processed_data, 'output_name', compress=True)
```
Saves processed data, optionally compressing the output.

### Data Loading
```python
loaded_data = dp.load_data('output_name')
```
Loads previously saved data.

### Stream Processing
```python
dp.enable_stream_mode()
streamed_data = dp.process_streaming_dataset(dataset)
```
Enables streaming mode and processes datasets in real-time.

## Dependencies and Requirements
- Python 3.7+
- \`datasets\`
- \`tensorflow\`
- \`scikit-learn\`
- \`numpy\`
- \`py7zr\` (for data compression)

## License
Daphne is licensed under the Apache 2.0 License.
