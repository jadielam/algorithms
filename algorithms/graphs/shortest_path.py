from typing import Hashable, Tuple, Dict, List

from dfs import topological_sort
import heapq

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
        d[v] = d[u] + w[(u, v)]
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
    d[s] = 0
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
        - d: The distance dict of each node.
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
                return False, d, parent
    
    return True, d, parent

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
    return d, parent

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
    visited = set()
    Q = [(0, s)]
    
    while Q: 
        t, u = heapq.heappop(Q) # The heapq.heappop happens more times than needed, because a node
                                # can potentially be added multiple times to the queue if its d[v]
                                # keeps improving. One way of improving on this is to run this algorithm
                                # by the number of entries in the adjacency list instead. But this
                                # is only possible if the graph is connected, otherwise, it is going
                                # to start copies of the nodes reachable from the source node before
                                # spitting the nodes with infinite distance, which will be at the
                                # end of the queue.
        visited.add(u)
        for v in adj[u]:
            if v not in visited:
                # Relaxing d of v, including heap change
                if d[v] > d[u] + w[(u, v)]:
                    d[v] = d[u] + w[(u, v)]
                    parent[v] = u
                    heapq.heappush(Q, (d[v], v))
    return d, parent
