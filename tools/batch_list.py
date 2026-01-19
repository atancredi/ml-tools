class BatchList:

    def __init__(self, batch_size, callback):
        if batch_size <= 0:
            raise ValueError("batch_size must be > 0")
        self.batch_size = batch_size
        self.callback = callback
        self._batch = []

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # flush only if no exception occurred
        if exc_type is None:
            self._flush()
        return False  # propagate exceptions

    def _flush(self):
        # ignore empty batches
        if not self._batch:
            return

        # prevent reference mutation bugs
        batch_to_process = self._batch
        self._batch = []

        self.callback(batch_to_process)

    def add(self, item) -> None:
        self._batch.append(item)
        if len(self._batch) >= self.batch_size:
            self._flush()


if __name__ == "__main__":

    with BatchList(3, lambda l: print(l)) as batch:
        for i in range(0, 10):
            batch.add(i)
