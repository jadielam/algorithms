from algorithms.combinatorics.generators import (
    permutations_recursive,
    permutations,
    combinations_recursive,
    combinations
)

def test_permutations_recursive():
    to_return = []
    permutations_recursive([1, 2, 3], [], 2, to_return)
    assert to_return == [[1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3,2]]

def test_permutations_recursive_large():
    to_return = []
    l = list(range(10))
    k = 5
    permutations_recursive(l, [], k, to_return)
    to_return_1 = permutations(l, k)
    to_return_1 = [list(p) for p in to_return_1]
    assert to_return == to_return_1

def test_combinations_recursive():
    to_return = []
    combinations_recursive([1, 2, 3], [], 2, to_return)
    assert to_return == [[1, 2], [1, 3], [2, 3]]

def test_combinations_recursive_large():
    to_return = []
    l = list(range(10))
    k = 5
    combinations_recursive(l, [], k, to_return)
    to_return_1 = combinations(l, k)
    to_return_1 = [list(p) for p in to_return_1]
    assert to_return == to_return_1
