from algorithms.sorting.countingsort import split_int_to_digits

def test_split_int_to_digits():
    assert split_int_to_digits(0) == [0]
    assert split_int_to_digits(1) == [1]
    assert split_int_to_digits(10) == [0, 1]
    assert split_int_to_digits(123) == [3, 2, 1]
    assert split_int_to_digits(1234567890) == [0, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert split_int_to_digits(12345678901234567890) == [0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1]