import pytest

from modules.calc import check_power_of_2
from modules.fibonachi import check_fibonacci
from modules.minmax import find_maximum_and_minimum
from modules.sumoffour import check_sum_of_four
from modules.task05 import find_maximal_subarray_sum
from tests import test_calc

data_to_process = [
    0,
    1,
    1,
    2,
    3,
    5,
    8,
    13,
    21,
    34,
    55,
    89,
    144,
    233,
    377,
    610,
    987,
    1597,
    2584,
    4181,
    6765,
]

# assert len(data_to_process) >= 3

# a, b, c = data_to_process[0], data_to_process[1], data_to_process[2]

# while len(data_to_process) >= 3:
#
#     a, b, c = data_to_process[0], data_to_process[1], data_to_process[2]
#     data_to_process = data_to_process[1:]
#     if not _check_window(a, b, c):
#         raise ValueError("Invalid data")

nums = [0, 17, 0, 0, 5, 5, 5, 0, 0, 0, 0, 0, 8]
k = 3
data = [1, 1, 2, 3]
# print(find_maximum_and_minimum("C:\\Users\\User\\Desktop\\output.txt"))
a, b, c, d = [-1, -2], [-1, -2], [-1, -2], [-1, -2]
fn = "output.txt"
g = [255, 0, 0, 128, 128]
l = 2
print(find_maximal_subarray_sum(g, l))
