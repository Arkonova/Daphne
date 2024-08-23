import dask.dataframe as dd

def process_large_csv(filepath, chunk_size=1000000):
    df = dd.read_csv(filepath, blocksize=chunk_size)
    df = df[df['column'] > 0]
    return df.compute()
def process_large_dataset(dataset, batch_size=1000, process_func=None):
    for i, batch in enumerate(dataset.batch(batch_size)):
        if process_func:
            batch = process_func(batch)
        yield batch.compute()