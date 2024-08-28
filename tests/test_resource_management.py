# tests/test_resource_management.py

import pytest
import pandas as pd
from unittest.mock import patch
from Daphne.resource_management import ResourceManager

@pytest.fixture
def sample_df():
    return pd.DataFrame({
        'feature1': [1, 2, 3, 4, 5],
        'feature2': [10, 20, 30, 40, 50]
    })

def test_check_memory():
    manager = ResourceManager()
    with patch('psutil.virtual_memory') as mock_memory:
        mock_memory.return_value.percent = 80
        with patch.object(manager, 'free_up_memory') as mock_free_up_memory:
            manager.check_memory()
            mock_free_up_memory.assert_called_once()

def test_free_up_memory():
    df = pd.DataFrame({
        'a': range(1000),
        'b': range(1000)
    })

    manager = ResourceManager()
    manager.free_up_memory(df)

    # Проверяем, что DataFrame пуст после освобождения памяти
    assert df.empty
def test_check_memory_no_action():
    manager = ResourceManager()
    with patch('psutil.virtual_memory') as mock_memory:
        mock_memory.return_value.percent = 50
        with patch.object(manager, 'free_up_memory') as mock_free_up_memory:
            manager.check_memory()
            mock_free_up_memory.assert_not_called()
