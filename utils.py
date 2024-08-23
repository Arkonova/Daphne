def analyze_dataset_structure(dataset):
    structure = {}
    for feature, feature_type in dataset.features.items():
        structure[feature] = str(feature_type)
    return structure