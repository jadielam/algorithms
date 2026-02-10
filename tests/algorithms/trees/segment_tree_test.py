"""
Tests for SegmentTree (range-sum) implementation.
"""

import random
import pytest
from algorithms.trees.segment_tree import SegmentTree


def test_build_and_query():
    data = [1, 2, 3, 4, 5]
    st = SegmentTree(data)
    assert len(st) == 5
    assert st.query(0, 4) == sum(data)
    assert st.query(1, 3) == 2 + 3 + 4
    assert st.query(2, 2) == 3


def test_point_update():
    data = [1, 2, 3, 4]
    st = SegmentTree(data)
    st.update(2, 10)  # set index 2 from 3 -> 10
    expected = [1, 2, 10, 4]
    assert st.query(0, 3) == sum(expected)
    assert st.query(2, 2) == 10


def test_single_element():
    st = SegmentTree([7])
    assert st.query(0, 0) == 7
    st.update(0, 3)
    assert st.query(0, 0) == 3


def test_empty_tree_query():
    st = SegmentTree()
    assert len(st) == 0
    # Query on empty tree returns 0
    assert st.query(0, 0) == 0


def test_invalid_ranges():
    st = SegmentTree([1, 2, 3])
    with pytest.raises(IndexError):
        st.query(-1, 2)
    with pytest.raises(IndexError):
        st.query(0, 3)
    with pytest.raises(IndexError):
        st.update(3, 5)


def test_random_queries_against_bruteforce():
    for _ in range(50):
        n = random.randint(1, 30)
        arr = [random.randint(-100, 100) for _ in range(n)]
        st = SegmentTree(arr)
        for _ in range(50):
            i = random.randint(0, n - 1)
            j = random.randint(0, n - 1)
            l, r = min(i, j), max(i, j)
            assert st.query(l, r) == sum(arr[l : r + 1])


def test_random_updates_and_queries():
    n = 100
    arr = [random.randint(0, 1000) for _ in range(n)]
    st = SegmentTree(arr)
    for _ in range(200):
        if random.random() < 0.6:
            # query
            l = random.randint(0, n - 1)
            r = random.randint(l, n - 1)
            assert st.query(l, r) == sum(arr[l : r + 1])
        else:
            idx = random.randint(0, n - 1)
            val = random.randint(-500, 1500)
            arr[idx] = val
            st.update(idx, val)
    # final full-range check
    assert st.query(0, n - 1) == sum(arr)
