from typing import Iterator, Hashable, List, Optional

class BinaryNode:
    def __init__(self, value, data = None):
        self.value = value
        self.data = data
        self.parent : Optional[BinaryNode]= None
        self.left : Optional[BinaryNode] = None
        self.right : Optional[BinaryNode] = None

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
    '''
    Returns the node has the given key. If no node is found with that key,
    returns None
    '''
    while root is not None and key != root.value:
        if key < root.value:
            root = root.left
        else:
            root = root.right
    return root

def tree_search_notnone(root: BinaryNode, key: Hashable) -> BinaryNode:
    '''
    Returns the node that has the given key. If no node is found with that key,
    returns the last valid node that the search visited.
    '''
    while root is not None and key != root.value:
        y = root
        if key < root.value:
            root = root.left
        else:
            root = root.right
    return root if root is not None else y

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

def tree_predecessor(x: BinaryNode) -> BinaryNode:
    '''
    x cannot be None
    '''
    #1. If node has left node, return maximum value of tree rooted in right node
    if x.left is not None:
        return tree_maximum(x.left)
    
    #2. Else return lowest ancestor of x that has a right child who is also an ancestor of x
    y = x.parent
    while y is not None and x is y.left:
        x = y
        y = y.parent
    return y

def tree_closest(root: BinaryNode, key: int) -> BinaryNode:
    '''
    Returns node in tree with value closest to key
    '''
    y = tree_search_notnone(root, key)
    if y.value == key:
        return y
    p = tree_predecessor(y)
    s = tree_successor(y)
    to_compare = [a for a in [p, s] if a is not None]
    min_distance = abs(y.value - key) 
    min_node = y
    for node in to_compare:
        if abs(node.value - key) < min_distance:
            min_distance = abs(node.value - key)
            min_node = node
    return min_node

def tree_closest_easier(root: BinaryNode, key: int) -> BinaryNode:
    """
    Returns the node in the tree with the value closest to key
    """
    closest_val_diff = float('inf')
    closest_node = None
    c_node = root
    while c_node is not None:
        if abs(c_node.value - key) < closest_val_diff:
            closest_val_diff = abs(c_node.value - key)
            closest_node = root
        if c_node.value < key:
            c_node = c_node.right
        elif c_node.value > key:
            c_node = c_node.left
        else:
            # No duplicates can exist in a binary search tree
            # so returning the first one is fine.
            return c_node

    # If there are multiple closest nodes, here we are returning the
    # first one that is minimum. We can modify the first if statement
    # logic to return multiple ones if needed.
    return closest_node

def lowest_common_ancestor(x: BinaryNode, y: BinaryNode) -> BinaryNode:
    '''
    Returns lowerst common ancestor node. Assumes x and y are not None
    '''
    seen = set()
    while x is not None:
        seen.add(x.value)
        x = x.parent
    
    c_node = y
    while c_node is not None:
        if c_node.value in seen:
            return c_node
        c_node = c_node.parent
    
    
def range_query(root: BinaryNode, low: int, high: int) -> List[int]:
    '''
    Returns as a list the values of all the nodes that fall within the
    [low, high] range
    '''
    #1. Find node A that is upper predecessor to low
    py = tree_search_notnone(root, low)
    p = tree_predecessor(py)
    p = p if p is not None else py
    
    #2. Find node B that is lower successor to high
    sy = tree_search_notnone(root, high)
    s = tree_successor(sy)
    s = s if s is not None else sy
    
    #3. Do in order traversal of graph from A to B, adding to list
    # all entries within range.  Do inorder traversal using stack.
    common_ancestor = lowest_common_ancestor(p, s)
    stack = [common_ancestor]
    left_added = set()
    to_return = []
    while stack:
        node = stack[-1]
        if not node.value in left_added:
            if node.left is not None and node.value >= low:
                stack.append(node.left)
            left_added.add(node.value)
        else:
            if node.value >= low and node.value <= high:
                to_return.append(node.value)
            stack.pop()
            if node.right is not None and node.value <= high:
                stack.append(node.right)
    
    return to_return

def range_query_easier(root: BinaryNode, low: int, high: int) -> List[int]:
    """
    Returns as a list the value of all the nodes that fall within the range
    [low, high]
    """
    def range_query_recursive(root: BinaryNode, low: int, high: int, to_return: List[int]):
        if root is not None:
            if root.val >= low and root.val <= high:
                to_return.append(root.val)
            if not root.val >= high:
                range_query_recursive(root.right, low, high, to_return)
            if not root.val <= low:
                range_query_recursive(root.left, low, high, to_return)
    
    to_return = []
    range_query_recursive(root, low, high, to_return)
    return to_return

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