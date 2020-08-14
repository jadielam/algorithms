from typing import Iterator

class BinaryNode:
    def __init__(self, value, data = None):
        self.value = value
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

def inorder_tree_walk(root: BinaryNode) -> Iterator:
    if root is not None:
        inorder_tree_walk(root.left)
        yield root
        inorder_tree_walk(root.right)



