from typing import Dict, List, Hashable, Tuple

def compute_residual(G: Dict[Hashable, List[Hashable]],
                    c: Dict[Tuple[Hashable, Hashable], float],
                    f: Dict[Tuple[Hashable, Hashable], float]):
    '''
    For each edge (u, v) in G:
    1. if f[u, v] < c[u, v], create forward edge (u, v) with
        cr[u, v] = c[u, v] - f[u, v]
    2. if f[u, v] > 0, create backward edge (v, u) with cr[v, u] = f[u, v]

    - Arguments:
        - G: adjacency list of original graph
        - c: dictionary of capacities of edges
        - f: dictionary of flows in edges
    
    - Returns:
        - Gr (Dict[Hashable, List[Hashable]]): adjacency list of residual graph
        - edge_type (Dict[Tuple[Hashable, Hashable], str]): dictionary that contains edge type for each edge
            in the residual graph.
        - cr (Dict[Tuple[Hashable, Hashable], float]): capacity of each edge in the residual graph.
    '''                    
    Gr = {}
    edge_type = {}
    cr = {}

    for u, adj in G.items():
        for v in adj:
            if f[u, v] < c[u, v]:
                if u not in Gr:
                    Gr[u] = []
                Gr[u].append(v)
                edge_type[u, v] = 'forward'
                cr[u, v] = c[u, v] - f[u, v]
            if f[u, v] > 0:
                if v not in Gr:
                    Gr[v] = []
                Gr[v].append(u)
                edge_type[v, u] = 'backward'
                cr[v, u] = f[u, v]

    return Gr, edge_type, cr

def get_shortest_path(Gr: Dict[Hashable, List[Hashable]], s: Hashable, t: Hashable) -> List[Hashable]:
    '''
    - Arguments:
        - Gr: Residual graph
        - s: source node id
        - t: sink node id
    
    - Returns:
        - p: List of nodes that make an s-t path in Gr.
            Returns None if no such path exists
    '''
    queue = [s]
    parent: Dict[Hashable, Hashable] = dict()
    visited = set()
    while queue:
        u = queue.pop(0)
        if u == t:
            break
        visited.add(u)
        if u in Gr:
            for v in Gr[u]:
                if not v in visited:
                    parent[v] = u
                    queue.append(v)
    
    if u != t:
        return None
    current_node = t
    path = [current_node]
    while current_node != s:
        current_node = parent[current_node]
        path.insert(0, current_node)
    return path

def augment(f: Dict[Tuple[Hashable, Hashable], float], 
            p: List[Hashable], 
            edge_type_d: Dict[Tuple[Hashable, Hashable], str], 
            cr: Dict[Tuple[Hashable, Hashable], float]):
    '''
    It does not return anything since it modifies flow f in place.

    - Arguments:
        - f: flow
        - p: s-t path in residual graph
        - edge_type_d: dictionary that contains edge types
        - cr: dictionary of capacity of edges in residual graph
    - Returns: 
        None
    '''
    #1. Find bottleneck value
    bottleneck_value = float('inf')
    for idx in range(1, len(p)):
        v = p[idx]
        u = p[idx - 1]
        c_edge = cr[u, v]
        if c_edge < bottleneck_value:
            bottleneck_value = c_edge
    
    for idx in range(1, len(p)):
        v = p[idx]
        u = p[idx - 1]
        edge_type = edge_type_d[u, v]
        if edge_type == 'forward':
            f[u, v] += bottleneck_value
        else:
            f[v, u] -= bottleneck_value

def edmonds_karp(G: Dict[Hashable, List[Hashable]],
                c: Dict[Tuple[Hashable, Hashable], float],
                s: Hashable,
                t: Hashable) -> Dict[Tuple[Hashable, Hashable], float]:
    '''
    This is the Edmonds-Karp algorithm that runs in O(VE^2). THe algorithm
    proceeeds like this:
    - Initialize flow to 0
    - Compute residual graph Gr of G
    - While there is an augmenting path p in Gr:
        - Pick path with the least number of edges
        - Augment flow across p
        - Update f
        - Recompute Gf
    - Return f

    - Arguments:
        - G: The original graph defined as an adjacency list
        - c: Dictionary containing the capacity of each node in 
            the graph.
        - s: Source node
        - t: Target (sink node)
    - Returns:
        - f (Dict[Tuple[Hashable, Hashable], float]): The optimal flow from s to t
        that satisfies the capacity constraints.
    '''

    #1. Create f and set it to zero
    f: Dict[Tuple[Hashable, Hashable], float] = {}
    for u, adj in G.items():
        for v in adj:
            f[u, v] = 0
    
    #2. Compute residual graph Gf
    Gr, edge_type, cr = compute_residual(G, c, f)
    
    p = get_shortest_path(Gr, s, t)
    while p is not None:
        augment(f, p, edge_type, cr)
        Gr, edge_type, cr = compute_residual(G, c, f)
        p = get_shortest_path(Gr, s, t)
    return f