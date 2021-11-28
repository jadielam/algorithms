from typing import List, Tuple
import bisect

class TreeNode:
    def __init__(self, ch: str = None):
        self.left = None
        self.right = None
        self.ch = str
    
def build_prefix(alphabet: List[Tuple[str, int]]) -> TreeNode:
    '''
    - Arguments:
        - alphabet: List of tuples of characters and frequencies of characters, in descending
        order by frequencies
    
    - Returns:
        - The root node of the prefix tree
    '''
    if len(alphabet) == 0:
        return None
    elif len(alphabet) == 1:
        left = TreeNode(alphabet[0][0])
        root = TreeNode()
        root.left = left
        return root
    elif len(alphabet) == 2:
        left = TreeNode(alphabet[0][0])
        right = TreeNode(alphabet[1][0])
        root = TreeNode()
        root.left = left
        root.right = right
        return root
    else:
        right_char = alphabet.pop()
        left_char = alphabet.pop()
        new_char = (0, right_char[1] + right_char[2])
        bisect.bisect_right()

    # TODO: Continue here
    pass

