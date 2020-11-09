from typing import List, Tuple

import pytest

from modules.minmax import find_maximum_and_minimum

path_to_file = "../output.txt"


@pytest.mark.parametrize(["value", "expected_result"], [(path_to_file, (0, 0))])
def test_find_maximum_and_minimum(value: str, expected_result: Tuple[str]):
    actual_result = find_maximum_and_minimum(value)

    assert actual_result == expected_result
