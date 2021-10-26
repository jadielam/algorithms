from typing import Hashable, Tuple, Dict, List

import algorithms.sorting.heap as heap
import algorithms.trees.disjoint_sets as disjoint_sets

def kruskal(adj: Dict[Hashable, List[Hashable]],
            w: Dict[Tuple[Hashable], float]) -> List[Tuple[Hashable, Hashable]]:
    '''
    Finds a minimum spaning tree in graph using Kruskal algorithm.
    This implementation runs in O(ElogE + (E + V))

    - Arguments:
        - adj: Graph represented as adjacency list. Assumes that nodes with no
        neighbors are present in the adjacency list.
        - w: Dictionary that contains weights of all edges in graph

    - Returns:
        - A: List of edges that form the minimum spanning tree
    '''
    A: List[Tuple[Hashable, Hashable]] = []
    dj = disjoint_sets.DisjointSets()
    sorted_edges = sorted(list(w.items()), key = lambda x: x[1])
    for v in adj.keys():
        dj.make_set(v)
    for ((u, v), _) in sorted_edges:
        if dj.find_set(u) != dj.find_set(v):
            A.append((u, v))
            dj.union(u, v)
    return A

def prim(adj: Dict[Hashable, List[Hashable]],
        w: Dict[Tuple[Hashable], float],
        r: Hashable) -> List[Tuple[Hashable, Hashable]]:
    '''
    TODO: Fix this algorithm to use heapq instead of custom
    implementation
    
    Finds a minimum spaning tree in graph using Prim's algorithm.
    Tree is rooted at r

    - Arguments:
        - adj: Graph represented as adjacency list. Assumes that nodes with no
        neighbors are present in the adjacency list.
        - w: Dictionary that contains weights of all edges in graph
        - r: root node

    - Retunrs:
        - A: List of edges that form the minimum spanning tree
    '''
    #1. Initializing data structures
    not_Q = set() # Keeps track of nodes not in queue.
    parent = {}
    key = {}
    for u in adj.keys():
        parent[u] = None
        key[u] = float('inf')
    key[r] = 0

    #2. Building heap and helper datastructures
    Q = [heap.PrioritizedItem(-key[u], idx, u) for idx, u in enumerate(key.keys())]
    entries_map = {pitem.item : pitem for pitem in Q}
    heap.build_max_heap(Q)
    
    #3. Run the algorithm
    while Q:
        heap_item = heap.extract_max(Q)
        u = heap_item.item
        not_Q.add(u)
        for v in adj[u]:
            if v not in not_Q and w[(u, v)] < key[v]:
                parent[v] = u
                key[v] = w[(u, v)]
                v_heap_position = entries_map[v].heap_position
                heap.heap_increase_key(Q, v_heap_position, -key[v])
    
    #4. Compile the list of edges that belong to tree. Note that
    # at this point not_Q contains all the vertices of the graph.
    A = [(v, parent[v]) for v in (not_Q - set([r]))]
    return A