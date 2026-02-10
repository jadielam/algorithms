"""
Unit tests for the treap data structure implementation.
Tests cover insertion, deletion, search, traversal, and structural properties.
"""

import pytest
from algorithms.trees.treap_ai import Treap, TreapNode


def test_treap_insert_single():
    """Test inserting a single value into an empty treap."""
    treap = Treap()
    treap.insert(5)
    assert treap.root is not None
    assert treap.root.val == 5


def test_treap_insert_multiple():
    """Test inserting multiple values maintains BST property."""
    treap = Treap()
    values = [5, 3, 7, 2, 4, 6, 8]
    for val in values:
        treap.insert(val)
    
    inorder = treap.inorder_walk()
    assert inorder == sorted(values)


def test_treap_insert_duplicates():
    """Test that duplicate insertions are not added."""
    treap = Treap()
    treap.insert(5)
    treap.insert(5)
    treap.insert(5)
    
    assert treap.inorder_walk() == [5]


def test_treap_search_existing():
    """Test searching for existing values."""
    treap = Treap()
    values = [5, 3, 7, 2, 4]
    for val in values:
        treap.insert(val)
    
    for val in values:
        node = treap.search(val)
        assert node is not None
        assert node.val == val


def test_treap_search_non_existing():
    """Test searching for non-existing values returns None."""
    treap = Treap()
    treap.insert(5)
    treap.insert(3)
    treap.insert(7)
    
    assert treap.search(1) is None
    assert treap.search(10) is None
    assert treap.search(6) is None


def test_treap_search_empty():
    """Test searching in an empty treap."""
    treap = Treap()
    assert treap.search(5) is None


def test_treap_delete_single():
    """Test deleting the only node in the treap."""
    treap = Treap()
    treap.insert(5)
    result = treap.delete(5)
    
    assert result is True
    assert treap.root is None
    assert treap.inorder_walk() == []


def test_treap_delete_existing():
    """Test deleting existing values maintains BST property."""
    treap = Treap()
    values = [5, 3, 7, 2, 4, 6, 8]
    for val in values:
        treap.insert(val)
    
    treap.delete(3)
    remaining = treap.inorder_walk()
    assert remaining == sorted([5, 7, 2, 4, 6, 8])


def test_treap_delete_root():
    """Test deleting the root node."""
    treap = Treap()
    values = [5, 3, 7]
    for val in values:
        treap.insert(val)
    
    treap.delete(5)
    remaining = treap.inorder_walk()
    assert remaining == [3, 7]
    assert treap.root is not None


def test_treap_delete_non_existing():
    """Test deleting non-existing values returns False."""
    treap = Treap()
    treap.insert(5)
    treap.insert(3)
    
    result = treap.delete(10)
    assert result is False
    assert treap.inorder_walk() == [3, 5]


def test_treap_delete_empty():
    """Test deleting from empty treap."""
    treap = Treap()
    result = treap.delete(5)
    assert result is False


def test_treap_multiple_operations():
    """Test a sequence of insert and delete operations."""
    treap = Treap()
    values = [5, 3, 7, 2, 4, 6, 8, 1, 9]
    
    for val in values:
        treap.insert(val)
    
    # Verify initial state
    assert treap.inorder_walk() == sorted(values)
    
    # Delete some values
    for val in [2, 5, 8]:
        treap.delete(val)
    
    expected = sorted([v for v in values if v not in [2, 5, 8]])
    assert treap.inorder_walk() == expected


def test_treap_heap_property_on_priorities():
    """Test that priorities maintain max-heap property."""
    treap = Treap()
    values = [5, 3, 7, 2, 4]
    for val in values:
        treap.insert(val)
    
    # Check that parent priority is >= children priorities
    def check_heap_property(node):
        if node is None:
            return True
        
        if node.left and node.left.priority > node.priority:
            return False
        if node.right and node.right.priority > node.priority:
            return False
        
        return check_heap_property(node.left) and check_heap_property(node.right)
    
    assert check_heap_property(treap.root)


def test_treap_bst_property():
    """Test that BST property is maintained."""
    treap = Treap()
    values = [5, 3, 7, 2, 4, 6, 8]
    for val in values:
        treap.insert(val)
    
    # Check BST property
    def check_bst_property(node, min_val=float('-inf'), max_val=float('inf')):
        if node is None:
            return True
        
        if not (min_val < node.val < max_val):
            return False
        
        return (check_bst_property(node.left, min_val, node.val) and
                check_bst_property(node.right, node.val, max_val))
    
    assert check_bst_property(treap.root)


def test_treap_inorder_walk():
    """Test inorder traversal returns sorted values."""
    treap = Treap()
    values = [5, 2, 8, 1, 9, 3]
    for val in values:
        treap.insert(val)
    
    result = treap.inorder_walk()
    assert result == sorted(values)


def test_treap_inorder_walk_empty():
    """Test inorder walk on empty treap."""
    treap = Treap()
    assert treap.inorder_walk() == []


def test_treap_height():
    """Test height calculation."""
    treap = Treap()
    assert treap.get_height() == 0
    
    treap.insert(5)
    assert treap.get_height() == 1
    
    treap.insert(3)
    treap.insert(7)
    assert treap.get_height() >= 2


def test_treap_large_insertion():
    """Test with a larger set of values."""
    treap = Treap()
    values = list(range(1, 101))
    
    # Insert in random order
    import random
    shuffled = values.copy()
    random.shuffle(shuffled)
    
    for val in shuffled:
        treap.insert(val)
    
    # Verify all values are present and in order
    assert treap.inorder_walk() == values


def test_treap_large_deletion():
    """Test deletion with larger dataset."""
    treap = Treap()
    values = list(range(1, 51))
    
    for val in values:
        treap.insert(val)
    
    # Delete every other element (even numbers: 2, 4, 6, ...)
    to_delete = values[::2]
    for val in to_delete:
        treap.delete(val)
    
    remaining = treap.inorder_walk()
    expected = [v for v in values if v not in to_delete]
    assert remaining == expected


def test_treap_node_representation():
    """Test string representation of TreapNode."""
    node = TreapNode(val=5, priority=0.75)
    str_repr = str(node)
    assert "val=5" in str_repr
    assert "priority" in str_repr


def test_treap_sequential_insertions():
    """Test inserting already sorted sequence."""
    treap = Treap()
    values = [1, 2, 3, 4, 5]
    for val in values:
        treap.insert(val)
    
    assert treap.inorder_walk() == values
    # With random priorities, tree should still be reasonably balanced
    height = treap.get_height()
    assert height <= len(values)  # Height should not exceed n


def test_treap_reverse_order_insertions():
    """Test inserting reverse sorted sequence."""
    treap = Treap()
    values = [5, 4, 3, 2, 1]
    for val in values:
        treap.insert(val)
    
    assert treap.inorder_walk() == sorted(values)


def test_treap_search_after_delete():
    """Test that search returns None after deletion."""
    treap = Treap()
    values = [5, 3, 7]
    for val in values:
        treap.insert(val)
    
    treap.delete(3)
    assert treap.search(3) is None
    assert treap.search(5) is not None
    assert treap.search(7) is not None
