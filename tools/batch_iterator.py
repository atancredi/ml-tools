class BatchIterator:
    def __init__(self, source, batch_size: int):
        if batch_size <= 0:
            raise ValueError("batch_size must be > 0")

        self.source = source
        self.batch_size = batch_size

    def __iter__(self):
        batch = []

        for item in self.source:
            batch.append(item)

            if len(batch) == self.batch_size:
                yield tuple(batch)
                batch = []

        if batch:
            yield tuple(batch)


if __name__ == "__main__":

    for batch in BatchIterator(range(0, 10), 3):
        print(len(batch))
