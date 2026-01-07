from algorithms.sorting.heap import (
    PrioritizedItem,
    build_max_heap,
    is_max_heap,
    heapsort,
    extract_max,
    heap_insert,
)


def priorities(lst):
    return [int(x.priority) for x in lst]


def test_build_and_is_max_heap_and_heapsort():
    items = [PrioritizedItem(i, i, str(i)) for i in [3, 1, 4, 2]]
    build_max_heap(items)
    assert is_max_heap(items, len(items))

    heapsort(items)
    assert priorities(items) == [1, 2, 3, 4]


def test_extract_and_insert():
    items = [PrioritizedItem(i, i, str(i)) for i in [2, 5, 1]]
    build_max_heap(items)
    max_elem = extract_max(items)
    assert max_elem.priority == 5
    # after extraction, remaining heap should still be valid (if non-empty)
    if items:
        assert is_max_heap(items, len(items))

    # test heap_insert
    heap_insert(items, 'x', 10)
    assert any(x.priority == 10 for x in items)
