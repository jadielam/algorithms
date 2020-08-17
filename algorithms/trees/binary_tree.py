from typing import Iterator, Hashable

class BinaryNode:
    def __init__(self, value, data = None):
        self.value = value
        self.data = data
        self.parent : BinaryNode = None
        self.left : BinaryNode = None
        self.right : BinaryNode = None

def inorder_tree_walk(root: BinaryNode) -> Iterator:
    if root is not None:
        yield from inorder_tree_walk(root.left)
        yield root
        yield from inorder_tree_walk(root.right)

def postorder_tree_walk(root: BinaryNode) -> Iterator:
    if root is not None:
        yield from postorder_tree_walk(root.right)
        yield root
        yield from postorder_tree_walk(root.left)

def tree_search_recursive(root: BinaryNode, key: Hashable) -> BinaryNode:
    if root is None or root.value == key:
        return root
    if key < root.value:
        return tree_search(root.left, key)
    else:
        return tree_search(root.right, key)

def tree_search(root: BinaryNode, key: Hashable) -> BinaryNode:
    while root is not None and key != root.value:
        if key < root.value:
            root = root.left
        else:
            root = root.right
    return root

def tree_minimum(root: BinaryNode) -> BinaryNode:
    '''
    root node cannot be None
    '''
    while root.left is not None:
        root = root.left
    return root

def tree_maximum(root: BinaryNode) -> BinaryNode:
    '''
    root node cannot be None
    '''
    while root.right is not None:
        root = root.right
    return root

def tree_successor(x: BinaryNode) -> BinaryNode:
    '''
    x node cannot be None
    '''
    # If node has right node, return minimum value of tree rooted in right node
    if x.right is not None:
        return tree_minimum(x.right)
    
    # Else, return the lowest ancestor of x that has a left child that is also
    # an ancestor of x. (remember that a node is an ancestor of itself)
    y = x.parent
    while y is not None and x is y.right:
        x = y
        y = y.parent
    return y 

def tree_insert(root: BinaryNode, z: BinaryNode) -> BinaryNode:
    '''
    Inserts node z into tree rooted at root

    - Returns:
        - new_root: Returns the new root of the tree
    '''
    new_root = root
    y = None
    x = root
    
    while x is not None:
        y = x
        if z.value < x.value:
            x = x.left
        else:
            x = x.right

    z.parent = y
    if y is None:
        new_root = z
    else:
        if z.value < y.value:
            y.left = z
        else:
            y.right = z

    return new_root

def tree_delete(root: BinaryNode, z: BinaryNode) -> BinaryNode:
    '''
    - Returns:
        - y: The node that is occupying the 
        - new_root
    '''
    #1. Determine which node childs will occupy the place of z
    # It will always be a descendant of z
    new_root = root
    if z.left is None or z.right is None:
        y: BinaryNode = z
    else:
        # in this specific case, it is guaranteed that the tree successor 
        # is a descendant of z with at most one child
        y: BinaryNode = tree_successor(z)

    #2. x is the node that will be left without a parent
    if y.left is not None:
        x: BinaryNode = y.left
    else:
        x: BinaryNode = y.right
    
    #3. Do the reconnection of parents and children
    # in the tree replacing y by y.parent and in x and
    # replacing y by x in y.parent
    if x is not None:
        x.parent = y.parent
    if y.parent is None:
        new_root = x
    elif y is y.parent.left:
        y.parent.left = x
    else:
        y.parent.right = x
    
    # If y is not z, then put the value of y in z
    # effectively removing z without changing the connections
    if y is not z:
        z.value = y.value
        z.data = y.data
    
    return y, new_root




    
