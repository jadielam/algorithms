from algorithms.trees.binary_tree import BinaryNode, tree_insert, inorder_tree_walk, tree_search


def build_bst(values):
    root = None
    for v in values:
        node = BinaryNode(v)
        root = tree_insert(root, node)
    return root


def test_tree_insert_and_inorder_walk_and_search():
    vals = [5, 3, 7, 2, 4]
    root = build_bst(vals)
    inorder_vals = [n.value for n in inorder_tree_walk(root)]
    assert inorder_vals == sorted(vals)
    assert tree_search(root, 4).value == 4
    assert tree_search(root, 100) is None
