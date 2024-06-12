from algorithms.sorting.quicksort import quick_sort

def test_quicksort():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    quick_sort(a, 0, len(a) - 1)
    assert a == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    quick_sort(a, 0, len(a) - 1)
    assert a == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    quick_sort(a, 0, len(a) - 1)
    assert a == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]
    quick_sort(a, 0, len(a) - 1)
    assert a == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0]
    quick_sort(a, 0, len(a) - 1)
    assert a == [0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0]
    quick_sort(a, 0, len(a) - 1)
    assert a == [0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_quick_sort_small_arrays():
    a = [1]
    quick_sort(a, 0, len(a) - 1)
    assert a == [1]
    
    a = [1, 2]
    quick_sort(a, 0, len(a) - 1)
    assert a == [1, 2]
    
    a = [2, 1]
    quick_sort(a, 0, len(a) - 1)
    assert a == [1, 2]
    
    a = [1, 2, 3]
    quick_sort(a, 0, len(a) - 1)
    assert a == [1, 2, 3]
    
    a = [3, 2, 1]
    quick_sort(a, 0, len(a) - 1)
    assert a == [1, 2, 3]
    
    a = [1, 3, 2]
    quick_sort(a, 0, len(a) - 1)
    assert a == [1, 2, 3]
    
    a = [2, 1, 3]
    quick_sort(a, 0, len(a) - 1)
    assert a == [1, 2, 3]
    
    a = [2, 3, 1]
    quick_sort(a, 0, len(a) - 1)
    assert a == [1, 2, 3]
    
    a = [3, 1, 2]
    quick_sort(a, 0, len(a) - 1)
    assert a == [1, 2, 3]
    
    a = [3, 2, 1]
    quick_sort(a, 0, len(a) - 1)
    assert a == [1, 2, 3]
    
    a = [1, 2, 3, 4]
    quick_sort(a, 0, len(a) - 1)
    assert a == [1, 2, 3, 4]
    
    a = [4, 3, 2, 1]
    quick_sort(a, 0, len(a) - 1)
    assert a == [1, 2, 3, 4]
    
    a = []
    quick_sort(a, 0, len(a) - 1)
    assert a == []