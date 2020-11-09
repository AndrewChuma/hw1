from typing import List

import pytest

from modules.task05 import find_maximal_subarray_sum


@pytest.mark.parametrize(
    ["value", "k", "expected_result"],
    [([127, 128, 256, 4], 4, 515), ([255, 0, 0, 128, 128], 2, 256)],
)
def test_find_maximum_and_minimum(value: List[int], k: int, expected_result: int):
    actual_result = find_maximal_subarray_sum(value)

    assert actual_result == expected_result
