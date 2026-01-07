from algorithms.graphs.msp import kruskal, prim


def test_kruskal_simple():
    adj = {
        1: [2, 3],
        2: [1, 3],
        3: [1, 2]
    }
    w = {(1,2): 1, (2,1):1, (1,3):2, (3,1):2, (2,3):3, (3,2):3}
    A = kruskal(adj, w)
    # MST of triangle should have 2 edges
    assert len(A) == 2
