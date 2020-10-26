from typing import Iterator, Hashable, List
from enum import Enum

class Color(Enum):
    RED = 1
    BLACK = 2

NilNode = RBNode(
    None,
    None
)

class RBNode:
    def __init__(self, value: Hashable, data = None):
        self.value = value
        self.data = data
        self.parent : RBNode = NilNode
        self.color : Color = Color.BLACK
        self.left : RBNode = NilNode
        self.right = RBNode = NilNode



def left_rotate(x: RBNode):
    y = x.right
    x.right = 

def tree_insert(root: RBNode, z: RBNode) -> RBNode:
    '''
    Inserts node z into tree rooted at root

    - Returns:
        - new_root: new root of the tree
    '''
    pass