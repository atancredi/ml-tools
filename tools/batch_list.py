class BatchList:

    def __init__(self, batch_size, callback):
        self.batch_size = batch_size
        self.callback = callback

    def __enter__(self):
        self.batch = []
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._flush()

    def _flush(self):
        if len(self.batch) == self.batch_size:
            self.callback(self.batch)
            self.batch.clear()
        
    def add(self, item):
        self.batch.append(item)
        self._flush()

if __name__ == "__main__":

    with BatchList(3, lambda l: print(l)) as batch:
        for i in range(0,10):
            batch.add(i)