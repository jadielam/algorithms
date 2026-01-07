from algorithms.graphs.bfs import bfs_connected, bfs_forest


def test_bfs_connected_basic():
    adj = {
        's': ['a', 'b'],
        'a': ['c'],
        'b': [],
        'c': []
    }
    parents, dist = bfs_connected(adj, 's', set())
    assert parents['a'] == 's'
    assert parents['b'] == 's'
    assert dist['c'] == 2


def test_bfs_forest_multiple_components():
    adj = {
        1: [2],
        2: [],
        3: [4],
        4: []
    }
    comps = bfs_forest(adj)
    # should return two connected components
    assert len(comps) == 2
