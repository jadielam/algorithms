from algorithms.sorting.insertionsort import insertion_sort


def test_insertion_sort_basic():
    a = [3, 1, 2]
    res = insertion_sort(a)
    assert res == [1, 2, 3]
    assert a == [1, 2, 3]


def test_insertion_sort_empty_and_single():
    a = []
    assert insertion_sort(a) == []
    a = [1]
    assert insertion_sort(a) == [1]
