# daphne/text_processing.py
import re

def clean_text(text):
    # Удаление пробелов и других символов
    text = text.strip()
    text = re.sub(r'\s+', ' ', text)
    return text.lower()

def normalize_text_column(dataset, column_name):
    # Применение стабилизации текста к указанной колонке
    return dataset.map(lambda x: {column_name: clean_text(x[column_name])})
