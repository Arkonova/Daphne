# daphne/batching.py
import os
import numpy as np
import shutil
import py7zr
import sys
def create_batches(dataset, batch_size=32):
    dataset_size = len(dataset)
    num_batches = dataset_size // batch_size + (1 if dataset_size % batch_size != 0 else 0)
    batches = []
    for i in range(num_batches):
        batch = dataset.select(range(i * batch_size, min((i + 1) * batch_size, dataset_size)))
        batches.append(batch)
    return batches
def save_batches(batches, folder_name='processed_batches', filename_prefix='batch', save_format='npz',
                 compression=None):
    current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    save_dir = os.path.join(current_dir, folder_name)
    print(save_dir)
    os.makedirs(save_dir, exist_ok=True)
    for i, batch in enumerate(batches):
        data = {key: np.array(batch[key]) for key in batch.features.keys()}
        filename = os.path.join(save_dir, f'{filename_prefix}_{i}.{save_format}')
        if save_format == 'npz':
            np.savez(filename, **data)
        elif save_format == 'hdf5':
            import h5py
            with h5py.File(filename, 'w') as hf:
                for key in data.keys():
                    hf.create_dataset(key, data=data[key])
        else:
            raise ValueError(f"Unsupported format: {save_format}")
    if compression:
        archive_name = os.path.join(current_dir, f'{folder_name}.{compression}')
        if compression == '7z':
            with py7zr.SevenZipFile(archive_name, 'w') as archive:
                archive.writeall(save_dir, arcname=folder_name)
        elif compression == 'zip':
            shutil.make_archive(archive_name, 'zip', save_dir)
        elif compression == None :
            print("Data packet saved without compression")
        else:
            raise ValueError(f"Unsupported compression format: {compression}")
        shutil.rmtree(save_dir)
def load_batches(filepaths, load_format='npz'):
    batches = []
    for filepath in filepaths:
        if load_format == 'npz':
            with np.load(filepath, allow_pickle=True) as data:
                batch = {key: data[key] for key in data}
        elif load_format == 'hdf5':
            import h5py
            with h5py.File(filepath, 'r') as hf:
                batch = {key: hf[key][:] for key in hf.keys()}
        else:
            raise ValueError(f"Unsupported format: {load_format}")
        batches.append(batch)
    return batches