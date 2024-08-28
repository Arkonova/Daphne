# tests/test_dataset_evaluation.py

import pytest
import pandas as pd
from Daphne.dataset_evaluation import DatasetEvaluator

@pytest.fixture
def sample_df():
    return pd.DataFrame({
        'feature1': [1, 2, 3, 4, 5],
        'feature2': [10, 20, 30, 40, 50],
        'target': [0, 1, 0, 1, 0]
    })

def test_plot_distribution(sample_df):
    evaluator = DatasetEvaluator()
    # Just testing if no exceptions are raised, plotting doesn't need to be tested.
    try:
        evaluator.plot_distribution(sample_df, 'feature1')
    except ValueError:
        pytest.fail("plot_distribution() raised ValueError unexpectedly!")

def test_check_correlations(sample_df):
    evaluator = DatasetEvaluator()
    try:
        evaluator.check_correlations(sample_df)
    except ValueError:
        pytest.fail("check_correlations() raised ValueError unexpectedly!")

def test_calculate_mutual_information(sample_df):
    evaluator = DatasetEvaluator()
    mi_scores = evaluator.calculate_mutual_information(sample_df, 'target')
    assert isinstance(mi_scores, pd.Series)
    assert mi_scores.shape[0] == sample_df.shape[1] - 1  # Excluding the target column

def test_plot_distribution_invalid_column(sample_df):
    evaluator = DatasetEvaluator()
    with pytest.raises(ValueError, match="Column 'invalid_column' not found in DataFrame."):
        evaluator.plot_distribution(sample_df, 'invalid_column')

def test_calculate_mutual_information_invalid_column(sample_df):
    evaluator = DatasetEvaluator()
    with pytest.raises(ValueError, match="Target column 'invalid_column' not found in DataFrame."):
        evaluator.calculate_mutual_information(sample_df, 'invalid_column')
