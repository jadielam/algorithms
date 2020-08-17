from typing import Dict, List, Any, Tuple, Set, Hashable

def bfs_forest(adj: Dict[Any, List[Any]]) -> List[Tuple[Any, Dict[Hashable, Hashable], Dict[Hashable, int]]]:
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
    visited.add(s)
    parents = {
        s: None
    }
    distance = {
        s: 0
    }

    while len(queue) > 0:
        node = queue.pop(0)
        if node in adj:
            for child in adj[node]:
                if not child in visited:
                    queue.append(child)
                    visited.add(child)
                    parents[child] = node
                    distance[child] = distance[node] + 1
    
    return parents, distance