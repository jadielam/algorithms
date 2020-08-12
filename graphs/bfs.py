from typing import Dict, List, Any, Tuple, Set, Hashable
from collections import Enum

def bfs_forest(adj: Dict[Any, List[Any]]):
    '''
    Given an adjacency list of a graph that is not necessarily connected 
    ( a forest ), it computes the parent dictionaries of all the connected
    components of the forest and returns them.

    - Arguments:
        - adj: Adjacency list of nodes
    '''
    visited = set()
    connected_components_data = []

    for node in adj.keys():
        if not node in visited:
            parents, distance = bfs_connected(adj, node, visited)
            connected_components_data.append((node, parents, distance))
    return connected_components_data

def bfs_connected(adj: Dict[Any, List[Hashable]], s: Any, visited: Set[Hashable]) -> Tuple[Dict[Hashable, Hashable], Dict[Hashable, int]]:
    '''
    - Arguments:
        - adj: Adjacency list of nodes
        - s: source node to use to compute the graph
        - color: dictionary of colors of nodes: white, gray and black
    
    - Returns:
        - parents: Dict[Hashable, Hashable]
        - distance: Dict[Hashable, int]
    '''
    queue = [s]
    parents = {}
    d = {}
    distance[s] = 0

    while len(queue) > 0:
        node = queue.pop(0)
        for child in adj[node]:
            if not child in visited:
                queue.append(child)
                visited.add(child)
                parent[child] = node
                distance[child] += d[node]
    
    return parents, distance
