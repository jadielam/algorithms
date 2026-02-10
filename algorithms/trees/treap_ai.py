"""
This module implements a treap (tree + heap), which is a randomized binary search tree
that maintains both BST and heap properties. A treap combines the benefits of binary
search trees and heaps by assigning random priorities to nodes and maintaining the
heap property on these priorities.

Key properties:
- Binary search tree property on values
- Max-heap property on randomly assigned priorities
- Average time complexity of O(log n) for search, insert, and delete operations
"""

from dataclasses import dataclass
from typing import Optional
import random


@dataclass
class TreapNode:
    """Represents a node in the treap with value, priority, and tree pointers."""
    val: int
    priority: float
    left: Optional['TreapNode'] = None
    right: Optional['TreapNode'] = None

    def __repr__(self):
        return f"TreapNode(val={self.val}, priority={self.priority:.4f})"


class Treap:
    """
    A treap is a randomized binary search tree that maintains a heap property
    based on randomly assigned priorities. This allows for balanced tree operations
    without explicit rebalancing logic like in AVL or Red-Black trees.
    """

    def __init__(self):
        """Initialize an empty treap."""
        self.root: Optional[TreapNode] = None

    def search(self, val: int) -> Optional[TreapNode]:
        """
        Search for a node with the given value.
        
        Average time complexity: O(log n)
        
        Args:
            val: The value to search for
            
        Returns:
            The TreapNode with the given value, or None if not found
        """
        return self._search_helper(self.root, val)

    def _search_helper(self, node: Optional[TreapNode], val: int) -> Optional[TreapNode]:
        """Helper function for recursive search."""
        if node is None:
            return None
        
        if node.val == val:
            return node
        elif val < node.val:
            return self._search_helper(node.left, val)
        else:
            return self._search_helper(node.right, val)

    def insert(self, val: int):
        """
        Insert a new value into the treap.
        
        - Creates a new node with the value and a random priority
        - Inserts it like a normal BST
        - Performs rotations to maintain the heap property on priorities
        
        Average time complexity: O(log n)
        
        Args:
            val: The value to insert
        """
        if self.search(val) is not None:
            # Don't insert duplicates
            return
        
        new_node = TreapNode(val=val, priority=random.random())
        
        if self.root is None:
            self.root = new_node
        else:
            self.root = self._insert_helper(self.root, new_node)

    def _insert_helper(self, node: Optional[TreapNode], new_node: TreapNode) -> TreapNode:
        """Helper function for recursive insertion."""
        if node is None:
            return new_node
        
        # Insert based on BST property
        if new_node.val < node.val:
            node.left = self._insert_helper(node.left, new_node)
            # Rotate right if left child has higher priority
            if node.left and node.left.priority > node.priority:
                node = self._rotate_right(node)
        else:
            node.right = self._insert_helper(node.right, new_node)
            # Rotate left if right child has higher priority
            if node.right and node.right.priority > node.priority:
                node = self._rotate_left(node)
        
        return node

    def delete(self, val: int) -> bool:
        """
        Delete a node with the given value from the treap.
        
        - Find the node to delete
        - Rotate it down to a leaf position using rotations
        - Remove the leaf
        
        Average time complexity: O(log n)
        
        Args:
            val: The value to delete
            
        Returns:
            True if a node was deleted, False if the value was not found
        """
        if self.search(val) is None:
            return False
        
        self.root = self._delete_helper(self.root, val)
        return True

    def _delete_helper(self, node: Optional[TreapNode], val: int) -> Optional[TreapNode]:
        """Helper function for recursive deletion."""
        if node is None:
            return None
        
        if val < node.val:
            node.left = self._delete_helper(node.left, val)
        elif val > node.val:
            node.right = self._delete_helper(node.right, val)
        else:
            # Found the node to delete
            # If it's a leaf, just return None
            if node.left is None and node.right is None:
                return None
            
            # If it has only one child, return that child
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            
            # If it has two children, rotate the higher priority child up
            if node.left.priority > node.right.priority:
                node = self._rotate_right(node)
                node.right = self._delete_helper(node.right, val)
            else:
                node = self._rotate_left(node)
                node.left = self._delete_helper(node.left, val)
        
        return node

    def _rotate_right(self, node: TreapNode) -> TreapNode:
        """
        Perform a right rotation at the given node.
        
        Before:        After:
            node          left_child
           /    \        /        \
        left   right  left_left  node
        / \              / \
        a   b            b  right
        """
        left_child = node.left
        node.left = left_child.right
        left_child.right = node
        return left_child

    def _rotate_left(self, node: TreapNode) -> TreapNode:
        """
        Perform a left rotation at the given node.
        
        Before:        After:
          node        right_child
         /    \      /          \
        left right  node       right_right
              / \   / \
             a   b left b
        """
        right_child = node.right
        node.right = right_child.left
        right_child.left = node
        return right_child

    def inorder_walk(self) -> list:
        """
        Return a list of values in inorder (sorted) traversal.
        
        Time complexity: O(n)
        
        Returns:
            List of values in sorted order
        """
        result = []
        self._inorder_helper(self.root, result)
        return result

    def _inorder_helper(self, node: Optional[TreapNode], result: list):
        """Helper function for inorder traversal."""
        if node is None:
            return
        
        self._inorder_helper(node.left, result)
        result.append(node.val)
        self._inorder_helper(node.right, result)

    def get_height(self) -> int:
        """
        Get the height of the treap.
        
        Returns:
            The height of the tree (empty tree has height 0)
        """
        return self._get_height_helper(self.root)

    def _get_height_helper(self, node: Optional[TreapNode]) -> int:
        """Helper function to calculate height."""
        if node is None:
            return 0
        return 1 + max(self._get_height_helper(node.left), 
                       self._get_height_helper(node.right))
