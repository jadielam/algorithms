from algorithms.sorting.selection import select_k

import pytest


def test_select_k():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert select_k(a, 0, len(a) - 1, 1) == 1
    assert select_k(a, 0, len(a) - 1, 2) == 2
    assert select_k(a, 0, len(a) - 1, 3) == 3
    assert select_k(a, 0, len(a) - 1, 4) == 4

    a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert select_k(a, 0, len(a) - 1, 1) == 0
    assert select_k(a, 0, len(a) - 1, 2) == 1

    a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert select_k(a, 0, len(a) - 1, 1) == 0
    assert select_k(a, 0, len(a) - 1, 2) == 1

def test_select_k_errors():
    with pytest.raises(ValueError):
        select_k([], 0, 0, 0)
    
    with pytest.raises(ValueError):
        select_k([], 0, 0, 1)
