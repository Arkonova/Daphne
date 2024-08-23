# daphne/streaming.py
from queue import Queue
from threading import Thread
from tqdm import tqdm
import traceback

class StreamProcessor:
    def __init__(self, process_func, total=None):
        self.queue = Queue()
        self.process_func = process_func
        self.running = False
        self.total = total
        self.progress_bar = tqdm(total=total, desc="Processing Data") if total else None

    def start(self):
        self.running = True
        Thread(target=self._process_stream).start()

    def _process_stream(self):
        while self.running or not self.queue.empty():
            if not self.queue.empty():
                data = self.queue.get()
                try:
                    self.process_func(data)
                    if self.progress_bar:
                        self.progress_bar.update(1)
                except Exception as e:
                    print("Error processing data:", e)
                    traceback.print_exc()

    def stop(self):
        self.running = False
        if self.progress_bar:
            self.progress_bar.close()

    def add_data(self, data):
        self.queue.put(data)

    def process_streaming_dataset(self, dataset):
        for example in dataset:
            self.add_data(example)
        self.stop()
