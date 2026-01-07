from algorithms.graphs.dfs import dfs_forest, dfs_forest_recursive, topological_sort


def test_dfs_forest_and_recursive_no_cycles():
    adj = {
        'u': ['v'],
        'v': ['w'],
        'w': []
    }
    parent, dtime, ftime = dfs_forest(adj)
    assert parent['v'] == 'u'
    assert 'u' in dtime and 'w' in ftime

    parent2, d2, f2, cycles = dfs_forest_recursive(adj)
    assert cycles == []


def test_topological_sort_simple():
    adj = {
        's': ['a', 'b'],
        'a': ['c'],
        'b': ['c'],
        'c': []
    }
    order = topological_sort(adj)
    # topological_sort returns list of tuples (node, finish_time)
    nodes = [n for n, _ in order]
    assert 'c' in nodes
