class Config:
    def __init__(self):
        self.parallel_jobs = -1
    def set_parallel_jobs(self, n_jobs):
        self.parallel_jobs = n_jobs
