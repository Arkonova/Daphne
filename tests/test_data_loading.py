# tests/test_data_loading.py

import pytest
import pandas as pd
import os
from Daphne.data_loading import DataLoader

@pytest.fixture
def temp_csv_file():
    # Create a temporary CSV file for testing
    file_path = 'temp_test_file.csv'
    df = pd.DataFrame({'col1': [1, 2], 'col2': ['a', 'b']})
    df.to_csv(file_path, index=False)
    yield file_path
    os.remove(file_path)

@pytest.fixture
def temp_json_file():
    # Create a temporary JSON file for testing
    file_path = 'temp_test_file.json'
    df = pd.DataFrame({'col1': [1, 2], 'col2': ['a', 'b']})
    df.to_json(file_path, orient='records')
    yield file_path
    os.remove(file_path)

def test_load_csv(temp_csv_file):
    df = DataLoader.load_data(temp_csv_file)
    assert isinstance(df, pd.DataFrame)
    assert 'col1' in df.columns

def test_load_json(temp_json_file):
    df = DataLoader.load_data(temp_json_file)
    assert isinstance(df, pd.DataFrame)
    assert 'col1' in df.columns

def test_load_unsupported_format():
    with pytest.raises(ValueError, match="Unsupported file format: .txt"):
        DataLoader.load_data('unsupported_file.txt')

def test_load_invalid_file():
    with pytest.raises(ValueError, match="Failed to load data from invalid_file.csv"):
        DataLoader.load_data('invalid_file.csv')
