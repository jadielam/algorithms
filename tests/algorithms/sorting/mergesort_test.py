from algorithms.sorting.mergesort import merge, merge_sort


def test_merge_two_sorted_lists():
    assert merge([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge([], [1]) == [1]
    assert merge([1], []) == [1]


def test_merge_sort_returns_sorted():
    a = [3, 1, 4, 2]
    res = merge_sort(a, 0, len(a))
    assert res == [1, 2, 3, 4]
    a = []
    assert merge_sort(a, 0, len(a)) == []
