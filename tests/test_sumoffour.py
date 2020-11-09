from typing import List

import pytest

from modules.sumoffour import check_sum_of_four


@pytest.mark.parametrize(
    ["A", "B", "C", "D", "expected_result"],
    [
        ([-1, -2], [-1, -2], [-1, -2], [-1, -2], 0),
        ([0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], 81),
    ],
)
def test_find_maximum_and_minimum(
    A: List[int], B: List[int], C: List[int], D: List[int], expected_result: int
):
    actual_result = check_sum_of_four(A, B, C, D)

    assert actual_result == expected_result
