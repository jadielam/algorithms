from typing import Hashable
from enum import Enum

class Color(Enum):
    RED = 1
    BLACK = 2

class NilNode:
    def __init__(self, parent = NIL):
        self.color : Color = Color.BLACK
        self.parent : RBNode = parent

NIL = NilNode()

class RBNode(object):
    def __init__(self, value: Hashable, data = None):
        self.value = value
        self.data = data
        self.parent : RBNode= NIL
        self.color : Color = Color.BLACK
        self.left : RBNode= NIL
        self.right : RBNode = NIL

def left_rotate(x: RBNode):
    y = x.right
    x.right = y.left
    y.parent = x.parent
    if x.parent is not NIL:
        if x is x.parent.left:
            x.parent.left = y
        elif x is x.parent.right:
            x.parent.right = y
    y.left = x
    x.parent = y
    return x

def right_rotate(y: RBNode):
    x = y.left
    y.left = x.right
    x.parent = y.parent
    if y.parent is not NIL:
        if y is y.parent.left:
            y.parent.left = x
        elif y is y.parent.right:
            y.parent.right = x
    x.right = y
    y.parent = x
    return y

def tree_insert(root: RBNode, z: RBNode) -> RBNode:
    '''
    Inserts node z into tree rooted at root

    - Returns:
        - new_root: new root of the tree
    '''
    pass