from joblib import Parallel, delayed

def parallel_apply(df, func, n_jobs=-1):
    return Parallel(n_jobs=n_jobs)(delayed(func)(row) for _, row in df.iterrows())
