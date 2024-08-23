from .utils import analyze_dataset_structure
def aggregate(df, by, agg_func):
    return df.groupby(by).agg(agg_func)

def filter_data(df, condition):
    return df.query(condition)

def transform_data(df, transform_func):
    return df.apply(transform_func, axis=1)

def prepare_data_for_task(dataset, task_type):
    structure = analyze_dataset_structure(dataset)
    needs_transformation = False

    if task_type == 'classification':
        if 'text' in structure and 'label' in structure:
            needs_transformation = True
            dataset = dataset.map(lambda x: {'input_ids': hash_text(x['text']), 'label': x['label']},
                                  remove_columns=[key for key in structure if key not in ['text', 'label']])

    elif task_type == 'text_generation':
        if 'text' in structure:
            needs_transformation = True
            dataset = dataset.map(lambda x: {'input_ids': hash_text(x['text'])},
                                  remove_columns=[key for key in structure if key != 'text'])

    elif task_type == 'image_classification':
        if 'image' in structure and 'label' in structure:
            needs_transformation = True
            dataset = dataset.map(lambda x: {'image': x['image'], 'label': x['label']},
                                  remove_columns=[key for key in structure if key not in ['image', 'label']])

    elif task_type == 'nlp':
        if 'text' in structure:
            needs_transformation = True
            dataset = dataset.map(lambda x: {'input_ids': hash_text(x['text'])},
                                  remove_columns=[key for key in structure if key != 'text'])

    if not needs_transformation:
        print("No conversion is required, the data will be used as is.")

    return dataset


def hash_text(text):
    return hash(text)
