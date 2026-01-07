from algorithms.graphs.shortest_path import initialize_single_source, dag_shortest_path, dijkstra, bellman_ford


def test_initialize_single_source():
    adj = {'s': [], 'a': []}
    d, p = initialize_single_source(adj, 's')
    assert d['s'] == 0
    assert d['a'] == float('inf')


def test_dag_shortest_path_and_dijkstra_and_bellman():
    adj = {
        's': ['a', 'b'],
        'a': ['c'],
        'b': ['c'],
        'c': []
    }
    w = {('s', 'a'): 1, ('s', 'b'): 5, ('a', 'c'): 2, ('b', 'c'): 1}
    d_dag, p_dag = dag_shortest_path(adj, w, 's')
    assert d_dag['c'] == 3

    d_dij, p_dij = dijkstra(adj, w, 's')
    assert d_dij['c'] == 3

    ok, d_bf, p_bf = bellman_ford(adj, w, 's')
    assert ok is True
    assert d_bf['c'] == 3
