import pytest
from bubblesort import bubble_sort

_test_data_bubble_sort = [
    pytest.param([], [], id="TC1: Exc10, empty list"),
    pytest.param([8], [8], id="TC2: Exc10, 1 item"),
    pytest.param([2, 9], [2, 9], id="TC3: Exc10, 2 items sorted"),
    pytest.param([9, 2], [2, 9], id="TC4: Exc10, 2 items unsorted"),
    pytest.param([3, 7, 1, 6, 4, 2, 5, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], id="TC5: Exc9, statement coverage 100%"),
    pytest.param(["peter", "Pal", "Evi", "michael", "Roxanne", "eva", "Eva"],
                 ["Eva", "Evi", "Pal", "Roxanne", "eva", "michael", "peter"], id="TC6: characters"),
    pytest.param([9.012345, 2.02], [2.02, 9.012345], id="TC7: float")
]


@pytest.mark.parametrize("mixed,expected", _test_data_bubble_sort)
def test_bubble_sort(mixed: list, expected: list):
    # Assert
    assert bubble_sort(mixed) == expected
