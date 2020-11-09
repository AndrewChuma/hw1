from collections import Sequence

import pytest

from modules.fibonachi import check_fibonacci


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [([8, 8, 16, 24, 40, 64], True), ([0, 0, 0, 0, 1, 1, 2, 3, 0], False)],
)
def test_fibonacci(value: Sequence, expected_result: bool):
    actual_result = check_fibonacci(value)

    assert actual_result == expected_result
