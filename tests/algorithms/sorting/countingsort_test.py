from algorithms.sorting.countingsort import split_int_to_digits
from algorithms.sorting.countingsort import radix_sort

def test_split_int_to_digits():
    assert split_int_to_digits(0) == [0]
    assert split_int_to_digits(1) == [1]
    assert split_int_to_digits(10) == [0, 1]
    assert split_int_to_digits(123) == [3, 2, 1]
    assert split_int_to_digits(1234567890) == [0, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert split_int_to_digits(12345678901234567890) == [0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1]

def test_sort_empty_list():
    assert radix_sort([]) == []

def test_sort_one_item_list():
    assert radix_sort([1]) == [1]

def test_sort_inverse_list():
    assert radix_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_sort_long_random_list():
    assert radix_sort([5, 4, 3, 2, 1, 9, 8, 7, 6, 0]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_sort_multiple_digits_list():
    to_sort = [123, 456, 789, 101, 202, 303, 404, 505, 606, 707, 808, 909]
    assert radix_sort(to_sort) == sorted(to_sort)