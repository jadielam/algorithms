from algorithms.trees.disjoint_sets import DisjointSets


def test_disjoint_sets_basic_union_find():
    ds = DisjointSets()
    for x in [1, 2, 3]:
        ds.make_set(x)
    ds.union(1, 2)
    assert ds.find_set(1) == ds.find_set(2)
    assert ds.find_set(3) != ds.find_set(1)
