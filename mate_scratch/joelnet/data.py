
from typing import Iterator, NamedTuple

import numpy as np

from numpy import ndarray

Batch = NamedTuple("Batch", [("inputs", ndarray), ("targets", ndarray)])


class DataIterator:
    def __call__(self, inputs: ndarray, targets: ndarray) -> Iterator:
        raise NotImplementedError

class BatchIterator(DataIterator):
    def __init__(self, shuffle: bool = True) -> None:
        self.shuffle = shuffle
    
    def __call__(self, inputs: ndarray, targets: ndarray) -> Iterator:
        yield Batch(inputs, targets)
        
        
class MiniBatchIterator(DataIterator):
    def __init__(self, batch_size: int = 32, shuffle: bool = True) -> None:
        self.batch_size = batch_size
        self.shuffle = shuffle

    def __call__(self, inputs: ndarray, targets: ndarray) -> Iterator:
        starts = np.arange(0, len(inputs), self.batch_size)
        if self.shuffle:
            np.random.shuffle(starts)

        for start in starts:
            end = start + self.batch_size
            batch_inputs = inputs[start:end]
            batch_targets = targets[start:end]
            yield Batch(batch_inputs, batch_targets)