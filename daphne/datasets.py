import datasets
import tensorflow_datasets as tfds

def load_hf_dataset(dataset_name, split='train', streaming=False):
    return datasets.load_dataset(dataset_name, split=split, streaming=streaming)

def load_tfds_dataset(dataset_name, split='train', streaming=False, as_supervised=True):
    return tfds.load(dataset_name, split=split, as_supervised=as_supervised, streaming=streaming)

def preprocess_for_model(dataset, task_type):
    if task_type == 'classification':
        dataset = dataset.map(lambda x: {'input_ids': x['text'], 'label': x['label']})
    elif task_type == 'nlp':
        dataset = dataset.map(lambda x: {'input_ids': x['text']})
    elif task_type == 'image_generation':
        dataset = dataset.map(lambda x: {'image': x['image']})
    return dataset
