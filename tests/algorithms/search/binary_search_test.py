from algorithms.search.binary_search import binary_search

def test_binary_search():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert binary_search(a, 0, len(a), 5) == 4
    assert binary_search(a, 0, len(a), 1) == 0
    assert binary_search(a, 0, len(a), 10) == 9
    assert binary_search(a, 0, len(a), 11) == -1
    assert binary_search(a, 0, len(a), 0) == -1
    assert binary_search(a, 0, len(a), 2) == 1
    assert binary_search(a, 0, len(a), 9) == 8
    assert binary_search(a, 0, len(a), 3) == 2
    assert binary_search(a, 0, len(a), 4) == 3
    assert binary_search(a, 0, len(a), 6) == 5
    assert binary_search(a, 0, len(a), 7) == 6
    assert binary_search(a, 0, len(a), 8) == 7
    assert binary_search(a, 0, len(a), 0) == -1
    assert binary_search(a, 0, len(a), 11) == -1
    assert binary_search(a, 0, len(a), 5) == 4
    assert binary_search(a, 0, len(a), 1) == 0
    assert binary_search(a, 0, len(a), 10) == 9
    assert binary_search(a, 0, len(a), 11) == -1
    assert binary_search(a, 0, len(a), 0) == -1
    assert binary_search(a, 0, len(a), 2) == 1
    assert binary_search(a, 0, len(a), 9) == 8
    assert binary_search(a, 0, len(a), 3) == 2
    assert binary_search(a, 0, len(a), 4) == 3
    assert binary_search(a, 0, len(a), 6) == 5