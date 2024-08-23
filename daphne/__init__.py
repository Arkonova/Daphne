import os
import sys
def set_working_directory():
    script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    os.chdir(script_dir)
set_working_directory()
from .loader import load_csv, load_json, load_from_db
from .preprocess import fill_missing, normalize, remove_duplicates, scale_data
from .processing import aggregate, filter_data, transform_data, prepare_data_for_task
from .big_data import process_large_csv, process_large_dataset
from .visualization import plot_data, plot_distribution
from .parallel import parallel_apply
from .streaming import StreamProcessor
from .config import Config
from .datasets import load_hf_dataset, load_tfds_dataset, preprocess_for_model
from .io import save_dataset
from .utils import analyze_dataset_structure
from .data_processing import standardize_data
from .clustering import cluster_data
from .text_processing import clean_text, normalize_text_column
from .batching import create_batches, save_batches