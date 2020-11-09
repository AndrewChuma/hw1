"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence
We guarantee, that the given sequence contain >= 0 integers inside.
"""
from collections import Sequence


def check_fibonacci(data: Sequence) -> bool:
    assert len(data) >= 3

    while len(data) >= 3:
        a, b, c = data[0], data[1], data[2]
        data = data[1:]
        if not ((a + b) == c):
            raise ValueError("Invalid data")
    return True
