from typing import Hashable, Tuple, Dict, List

from dfs import topological_sort
import algorithms.sorting.heap as heap

def relax(u: Hashable, v: Hashable, 
            d: Dict[Hashable, float], 
            w: Dict[Tuple[Hashable], float],
            parent: Dict[Hashable, Hashable]):
    '''
    - Arguments:
        - u: Graph node id
        - v: Graph node id
        - w: Dictionary that contains weights of all edges in graph
        - parent: Dictionary that keeps track of what node is parent
        of what node.
    '''
    if d[v] > d[u] + w[(u, v)]:
        d[v] = d[u] + w([u, v])
        parent[v] = u

def initialize_single_source(adj: Dict[Hashable, List[Hashable]], s: Hashable):
    '''
    - Arguments:
        - adj: Graph represented as adjacency list. Assumes that nodes with no
        neighbors are present in the adjacency list.
        - s: source node
    '''
    d = {}
    p = {}
    for v in adj.keys():
        d[v] = float('inf')
        p[v] = None
    return d, p

def bellman_ford(adj: Dict[Hashable, List[Hashable]], 
                w: Dict[Tuple[Hashable], float],
                s: Hashable) -> Tuple[bool, Dict[Hashable, Hashable]]:
    '''
    Computes the shortest path from node s to all other nodes in the graph.
    Graph can contain negative edges. Graph must be a directed graph. If graph
    contains negative cycle, then the result is undefined and it returns false

    - Arguments:
        - adj: Graph represented as adjacency list. Assumes that nodes with no
        neighbors are present in the adjacency list.
         - w: Dictionary that contains weights of all edges in graph
        - s: source node
    
    - Returns:
        - result: bool. If graph contains valid shortest paths (no negative cycle
        in graph), returns True, otherwise returns False
        - parent: Dictionary that keeps track of what node is parent
        of what node.
    '''
    d, parent = initialize_single_source(adj, s)
    for _ in range(len(adj) - 1):
        for u in adj.keys():
            for v in adj[u]:
                relax(u, v, d, w, parent)
    
    for u in adj.keys():
        for v in adj[u]:
            if d[v] > d[u] + w[(u, v)]:
                return False, {}
    
    return True, parent

def dag_shortest_path(adj: Dict[Hashable, List[Hashable]], 
                w: Dict[Tuple[Hashable], float],
                s: Hashable) -> Dict[Hashable, Hashable]:
    '''
    Assumes that the input graph is a directed acyclic graph.

    - Arguments:
        - adj: Graph represented as adjacency list. Assumes that nodes with no
        neighbors are present in the adjacency list.
         - w: Dictionary that contains weights of all edges in graph
        - s: source node
    
    - Returns:
        - parent: Dictionary that keeps track of what node is parent
        of what node.
    '''
    sorted_entries = topological_sort(adj)
    d, parent = initialize_single_source(adj, s)
    for u, _ in sorted_entries:
        for v in adj[u]:
            relax(u, v, d, w, parent)
    return parent

def dijkstra(adj: Dict[Hashable, List[Hashable]], 
                w: Dict[Tuple[Hashable], float],
                s: Hashable) -> Tuple[bool, Dict[Hashable, Hashable]]:
    '''
    Computes the shortest path from node s to all other nodes in the graph.
    Graph must be a directed graph. If graph
    contains negative cycle, then the result is undefined and it will break
    the algorithm

    - Arguments:
        - adj: Graph represented as adjacency list. Assumes that nodes with no
        neighbors are present in the adjacency list.
         - w: Dictionary that contains weights of all edges in graph
        - s: source node
    
    - Returns:
        - parent: Dictionary that keeps track of what node is parent
        of what node.
    '''
    d, parent = initialize_single_source(adj, s)
    S = set()
    heap_entries = [heap.PrioritizedItem(-d[node], node) for node in d.keys()]
    entries_map = {pitem.item : pitem for pitem in heap_entries}
    Q = heap.build_max_heap(heap_entries)
    while Q:
        max_entry = heap.extract_max(Q)
        u = max_entry.item
        S.add(u)
        for v in adj[u]:
            # Relaxing d of v, including heap change
            if d[v] > d[u] + w[(u, v)]:
                d[v] = d[u] + w([u, v])
                parent[v] = u
                v_heap_position = entries_map[v].heap_position
                heap.heap_increase_key(Q, v_heap_position, d[v])
    
    return parent