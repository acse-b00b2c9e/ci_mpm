import numpy as np

__all__ = ["my_sum"]


def my_sum(iterable):
    tot = 0
    for i in iterable:
        tot += i
    return tot


def my_sin(x):
    return np.sin(x)
