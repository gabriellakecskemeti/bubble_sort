from bubblesort import bubble_sort
import pytest

_test_data_bubble_sort = [
    pytest.param([], [], id="TC1: empty list"),
    pytest.param([8], [8], id="TC2: 1 item"),
    pytest.param([2, 9], [2, 9], id="TC4: 2 items sorted"),
    pytest.param([9, 2], [2, 9], id="TC4: 2 items mixed")
]

@pytest.mark.parametrize("mixed,expected", _test_data_bubble_sort)
def test_bubble_sort(mixed: list, expected: list):
    # Assert
    assert bubble_sort(mixed) == expected
